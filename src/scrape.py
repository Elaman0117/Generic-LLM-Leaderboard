#!/usr/bin/env python3
"""
Scraper for Artificial Analysis LLM Leaderboard.

Extracts the full model dataset (Status: All, including deprecated models)
from Artificial Analysis at https://artificialanalysis.ai/leaderboards/models?status=all.

Architecture:
1. Artificial Analysis renders Next.js RSC (React Server Components). The page payload
   carries dynamic encrypted data manifests for complete model listings:
   {"path": "/data/<hash>.txt", "key": "<hex>"} and releases metadata.
2. The encrypted payload is fetched and decrypted using AES-GCM (IV = SHA-256(key)[:12], tag=128)
   and decompressed with GZip stream decompression.
3. Unpacks nested scores into canonical benchmark metric names (e.g. hle, gpqa, scicode).
4. Associates each model with its release date, release slug, creator, and pricing/speed metrics.
5. Saves the complete dataset to output/raw_data.json.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
from typing import Dict, List, Optional

URL = "https://artificialanalysis.ai/leaderboards/models?status=all"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "raw_data.json")
MIN_MODELS_EXPECTED = 100

# Canonical benchmark metric name mapping
SCORE_KEY_MAP = {
    "humanitys-last-exam": "hle",
    "hle-diamond": "hleDiamond",
    "gpqa-diamond": "gpqa",
    "critpt": "critpt",
    "critpt-v2-hard": "critptV2Hard",
    "critpt-v2": "critptV2Hard",
    "aime-2025": "aime2025",
    "scicode": "scicode",
    "livecodebench": "livecodebench",
    "frontiercode": "frontiercode",
    "frontiercode-2-0": "frontiercode20",
    "terminalbench-hard": "terminalbenchHard",
    "terminalbench-2-1": "terminalBench21",
    "terminalbench-4-0": "terminalBench40",
    "terminal-bench-science": "terminalbenchScience",
    "tau2-bench": "tau2",
    "tau3-banking": "tauBanking",
    "automationbench-aa": "automationbench",
    "aa-briefcase": "briefcase",
    "gdpval-aa-normalized": "gdpvalNormalized",
    "gdp-pdf": "gdpPdf",
    "artificial-analysis-long-context-reasoning": "lcr",
    "mlcr-aa": "mlcr",
    "mmmu-pro": "mmmuPro",
    "code2video-aa": "code2video",
    "aa-3d": "aa3d",
    "omniscience-accuracy": "omniscienceAccuracy",
    "omniscience-non-hallucination": "omniscienceNonHallucination",
    "ifbench": "ifbench",
    "aa-analyst-agent": "analystAgent",
    "apex-agents-aa": "apexAgents",
    "enterprise-ops-gym-aa": "enterpriseOps",
    "itbench-aa": "itbenchSre",
    "harvey-lab-aa": "harveyLab",
    "healthbench": "healthbench",
    "healthbench-professional": "healthbenchProfessional",
    "vials-aa": "vials",
    "mka": "vials",
}


def _unpack_scores(model: dict):
    """Unpack nested benchmark scores from 'scores' dict onto model object."""
    if not isinstance(model, dict):
        return
    scores = model.get("scores")
    if isinstance(scores, dict):
        for k, v in scores.items():
            mapped = SCORE_KEY_MAP.get(k)
            if mapped and mapped not in model and v is not None:
                model[mapped] = v
            if k not in model and v is not None:
                model[k] = v


def _extract_balanced_json(text: str, start_index: int) -> tuple:
    """Extract a balanced JSON bracket or brace starting at start_index."""
    opening = text[start_index]
    closing = "]" if opening == "[" else "}"
    depth = 0
    in_str = False
    escape = False

    for i in range(start_index, len(text)):
        c = text[i]
        if escape:
            escape = False
            continue
        if c == "\\":
            escape = True
            continue
        if c == '"':
            in_str = not in_str
            continue
        if not in_str:
            if c == opening:
                depth += 1
            elif c == closing:
                depth -= 1
                if depth == 0:
                    return json.loads(text[start_index:i + 1]), i + 1

    raise ValueError(f"Unmatched {opening} in JSON text")


def fetch_page_payload() -> str:
    """Fetch RSC or HTML payload from the leaderboard URL."""
    req = urllib.request.Request(
        URL,
        headers={
            "RSC": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "*/*",
        }
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def decrypt_manifest_models(manifest_url: str, key_hex: str) -> List[dict]:
    """Decrypt the AES-GCM + gzip compressed models payload using Node.js."""
    node_script = f"""
async function run() {{
  const resp = await fetch({json.dumps(manifest_url)});
  if (!resp.ok) throw new Error('Failed to fetch manifest data: ' + resp.status);
  const r = await resp.arrayBuffer();
  const keyHex = {json.dumps(key_hex)};
  const n = new Uint8Array(keyHex.length / 2);
  for (let i = 0; i < keyHex.length; i += 2) {{
    n[i / 2] = parseInt(keyHex.slice(i, i + 2), 16);
  }}
  const digest = await crypto.subtle.digest('SHA-256', n.buffer);
  const a = new Uint8Array(digest).slice(0, 12);
  const s = await crypto.subtle.importKey('raw', n.buffer, {{ name: 'AES-GCM' }}, false, ['decrypt']);
  const i = await crypto.subtle.decrypt({{ name: 'AES-GCM', iv: a.buffer, tagLength: 128 }}, s, r);
  const c = new DecompressionStream('gzip');
  const l = c.writable.getWriter();
  l.write(new Uint8Array(i));
  l.close();
  const text = await new Response(c.readable).text();
  process.stdout.write(text);
}}
run().catch(e => {{ console.error(e); process.exit(1); }});
"""
    res = subprocess.run(["node", "-e", node_script], capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def scrape_leaderboard() -> List[dict]:
    """Scrape the latest models dataset from Artificial Analysis."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Load existing slugs, release dates, and historical timing metrics for stable continuity
    existing_slugs = {}
    existing_dates = {}
    existing_timing = {}
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            for m in old_data:
                name = m.get("name")
                slug = m.get("slug")
                if name:
                    if slug:
                        existing_slugs[name] = slug
                    if m.get("releaseDate"):
                        existing_dates[name] = m["releaseDate"]
                    timing = {}
                    for tk in [
                        "medianEndToEndResponseTimeSeconds",
                        "medianReasoningTimeSeconds",
                        "medianTimeToFirstTokenSeconds",
                        "medianTimeToFirstAnswerTokenSeconds",
                        "intelligenceIndexTimePerTask",
                    ]:
                        if m.get(tk) is not None:
                            timing[tk] = m[tk]
                    if timing:
                        existing_timing[name] = timing
                        if slug:
                            existing_timing[slug] = timing
        except Exception:
            pass

    # If existing_timing has few entries, attempt fallback to git HEAD for historical timing
    if len(existing_timing) < 100:
        try:
            head_out = subprocess.check_output(
                ["git", "show", "HEAD:output/raw_data.json"],
                stderr=subprocess.DEVNULL,
            ).decode("utf-8")
            head_data = json.loads(head_out)
            for m in head_data:
                name = m.get("name")
                slug = m.get("slug")
                timing = {}
                for tk in [
                    "medianEndToEndResponseTimeSeconds",
                    "medianReasoningTimeSeconds",
                    "medianTimeToFirstTokenSeconds",
                    "medianTimeToFirstAnswerTokenSeconds",
                    "intelligenceIndexTimePerTask",
                ]:
                    if m.get(tk) is not None:
                        timing[tk] = m[tk]
                if timing:
                    if name and name not in existing_timing:
                        existing_timing[name] = timing
                    if slug and slug not in existing_timing:
                        existing_timing[slug] = timing
        except Exception:
            pass

    print(f"[1/4] Fetching payload from {URL} ...")
    content = fetch_page_payload()

    # Extract manifest
    print("[2/4] Parsing manifest and releases metadata ...")
    m_manifest = re.search(r'"manifest":\s*(\{"path":[^}]+\})', content)
    if not m_manifest:
        # Check escaped version if inside self.__next_f
        m_manifest = re.search(r'\\"manifest\\":\s*(\{\\"path\\":[^}]+\})', content)
        if m_manifest:
            manifest_str = m_manifest.group(1).replace('\\"', '"')
            manifest = json.loads(manifest_str)
        else:
            raise RuntimeError("Could not find manifest in page payload.")
    else:
        manifest = json.loads(m_manifest.group(1))

    manifest_path = manifest["path"]
    manifest_key = manifest["key"]
    manifest_url = manifest_path if manifest_path.startswith("http") else f"https://artificialanalysis.ai{manifest_path}"
    print(f"  Manifest path: {manifest_path} (key: {manifest_key[:8]}...)")

    # Extract releases
    releases = []
    pos_rel = content.find('"releases":[')
    if pos_rel != -1:
        start_idx = pos_rel + len('"releases":')
        releases, _ = _extract_balanced_json(content, start_idx)
    else:
        pos_rel = content.find('\\"releases\\":[')
        if pos_rel != -1:
            clean_content = content.replace('\\"', '"')
            pos_rel2 = clean_content.find('"releases":[')
            start_idx = pos_rel2 + len('"releases":')
            releases, _ = _extract_balanced_json(clean_content, start_idx)

    release_date_map = {}
    for r in releases:
        slug = r.get("slug")
        rdate = r.get("releaseDate")
        if slug and rdate:
            release_date_map[slug] = rdate
    print(f"  Extracted {len(releases)} release entries ({len(release_date_map)} dated).")

    # Decrypt models payload
    print("[3/4] Decrypting model dataset ...")
    raw_models = decrypt_manifest_models(manifest_url, manifest_key)
    print(f"  Successfully decrypted {len(raw_models)} models from payload.")

    # Process and normalize models
    models = []
    for m in raw_models:
        name = m.get("name") or m.get("shortName") or "Unknown"
        rel = m.get("release") or {}
        release_slug = rel.get("slug") or ""
        m["releaseSlug"] = release_slug
        suffix = m.get("suffix")

        # Set model slug
        if name in existing_slugs:
            m["slug"] = existing_slugs[name]
        elif release_slug:
            if suffix:
                clean_suf = re.sub(r'[^a-zA-Z0-9]+', '-', suffix.lower()).strip('-')
                m["slug"] = f"{release_slug}-{clean_suf}"
            else:
                m["slug"] = release_slug
        else:
            m["slug"] = re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')

        # Set release date
        if release_slug in release_date_map:
            m["releaseDate"] = release_date_map[release_slug]
        elif m.get("slug") in release_date_map:
            m["releaseDate"] = release_date_map[m["slug"]]
        elif name in existing_dates:
            m["releaseDate"] = existing_dates[name]

        # Model creator
        if m.get("modelCreatorName") and not m.get("creator"):
            m["creator"] = m["modelCreatorName"]

        # Latency / speed compatibility aliases
        if m.get("outputSpeed") is not None and "medianOutputTokensPerSecond" not in m:
            m["medianOutputTokensPerSecond"] = m["outputSpeed"]
        if m.get("timeToFirstToken") is not None and "medianTimeToFirstTokenSeconds" not in m:
            m["medianTimeToFirstTokenSeconds"] = m["timeToFirstToken"]
        if m.get("timeToFirstAnswerToken") is not None and "medianTimeToFirstAnswerTokenSeconds" not in m:
            m["medianTimeToFirstAnswerTokenSeconds"] = m["timeToFirstAnswerToken"]

        # Restore historical timing metrics (e.g. medianEndToEndResponseTimeSeconds)
        m_slug = m.get("slug")
        hist = existing_timing.get(name) or (existing_timing.get(m_slug) if m_slug else None)
        if hist:
            for tk, tv in hist.items():
                if m.get(tk) is None:
                    m[tk] = tv

        # For any model missing medianEndToEndResponseTimeSeconds where speed is available:
        if m.get("medianEndToEndResponseTimeSeconds") is None and m.get("medianOutputTokensPerSecond") and m["medianOutputTokensPerSecond"] > 0:
            ttft = m.get("medianTimeToFirstTokenSeconds") or 2.0
            ttat = m.get("medianTimeToFirstAnswerTokenSeconds")
            if ttat is not None and ttat > ttft:
                if m.get("medianReasoningTimeSeconds") is None:
                    m["medianReasoningTimeSeconds"] = ttat - ttft
                start_time = ttat
            else:
                start_time = ttft
            m["medianEndToEndResponseTimeSeconds"] = start_time + (500.0 / m["medianOutputTokensPerSecond"])

        # Unpack benchmark scores
        _unpack_scores(m)
        models.append(m)

    # Validation
    models_with_intel = sum(1 for m in models if m.get("intelligenceIndex") is not None)
    models_with_benchmarks = sum(1 for m in models if m.get("hle") is not None or m.get("gpqa") is not None)
    deprecated_count = sum(1 for m in models if m.get("deprecated"))
    dated_count = sum(1 for m in models if m.get("releaseDate"))

    if len(models) < MIN_MODELS_EXPECTED or models_with_intel < 50 or models_with_benchmarks < 50:
        raise RuntimeError(
            f"Extraction validation failed: {len(models)} models extracted "
            f"(expected >= {MIN_MODELS_EXPECTED}), {models_with_intel} with intelligenceIndex, "
            f"{models_with_benchmarks} with benchmarks."
        )

    print(f"  Validated: {len(models)} models ({models_with_intel} with intelligenceIndex, "
          f"{models_with_benchmarks} with core benchmarks, {deprecated_count} deprecated, "
          f"{dated_count} dated).")

    # Sample model info
    sample_model = next((x for x in models if x.get("intelligenceIndex") is not None), models[0])
    print(f"  Sample: {sample_model.get('name')}, "
          f"creator={sample_model.get('modelCreatorName')}, "
          f"intelIndex={sample_model.get('intelligenceIndex')}, "
          f"inputPrice=${sample_model.get('price1mInputTokens')}, "
          f"outputPrice=${sample_model.get('price1mOutputTokens')}")

    print(f"[4/4] Saving to {OUTPUT_FILE} ...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(models, f, ensure_ascii=False, indent=2)

    print(f"Done! {len(models)} models successfully saved to {OUTPUT_FILE}.")
    return models


if __name__ == "__main__":
    try:
        data = scrape_leaderboard()
        if not data or len(data) < MIN_MODELS_EXPECTED:
            raise RuntimeError(f"Scraping returned insufficient models: {len(data) if data else 0}")
    except Exception as e:
        print(f"Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
