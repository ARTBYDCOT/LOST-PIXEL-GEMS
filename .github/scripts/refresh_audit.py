#!/usr/bin/env python3
"""
Best-effort web-scan to update verification_status for contracts.json.
This script does NOT use an API key; it parses explorer pages for "Contract: Verified/Unverified" markers.
"""
import json
import requests
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_PATH = ROOT / 'documentation' / 'lost-pixel-gems-docs' / 'contracts.json'
AUDIT_STATUS_PATH = ROOT / '.github' / 'audit-status.json'

EXPLORERS = {
    1: 'https://etherscan.io/address/{addr}#code',
    8453: 'https://basescan.org/address/{addr}#code'
}

USER_AGENT = 'lost-pixel-gems-audit-bot/1.0 (+https://github.com/ARTBYDCOT/LOST-PIXEL-GEMS)'

now_iso = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'


def infer_status_from_html(html: str):
    low = html.lower()
    if 'ethereum account (invalid address)' in low or 'invalid address' in low:
        return 'invalid_address'
    if 'contract: verified' in low or 'contract source code verified' in low or 'verified contract' in low:
        return 'verified'
    if 'contract: unverified' in low or 'contract: unverified |' in low:
        return 'unverified'
    # fallback heuristics
    if 'contract' in low and 'source code' in low and 'verified' in low:
        return 'verified'
    return 'unknown'


def main():
    if not CONTRACTS_PATH.exists():
        print('contracts.json not found at', CONTRACTS_PATH)
        return

    data = json.loads(CONTRACTS_PATH.read_text())
    updated = False

    for c in data.get('contracts', []):
        addr = c.get('address')
        chain = c.get('chainId', 1)
        if not addr:
            continue
        try:
            addr_norm = addr.strip()
            url_template = EXPLORERS.get(chain, EXPLORERS[1])
            url = url_template.format(addr=addr_norm)
            headers = {'User-Agent': USER_AGENT}
            resp = requests.get(url, headers=headers, timeout=20)
            status = infer_status_from_html(resp.text) if resp.status_code == 200 else 'unknown'
        except Exception as e:
            url = url_template.format(addr=addr_norm)
            status = 'unknown'

        # Map explorer-derived statuses into the same taxonomy used in contracts.json
        prev = c.get('verification_status')
        if prev != status or c.get('source_url') != url or c.get('last_checked') != now_iso:
            c['verification_status'] = status
            c['source_url'] = url
            c['last_checked'] = now_iso
            c['check_method'] = 'best-effort-web-scan'
            updated = True
            print(f"Updated {addr} -> {status}")

    if updated:
        CONTRACTS_PATH.write_text(json.dumps(data, indent=2))
        print('Wrote updates to', CONTRACTS_PATH)
    else:
        print('No updates')

    # Ensure audit-status.json exists minimally
    if not AUDIT_STATUS_PATH.exists():
        AUDIT_STATUS_PATH.write_text(json.dumps({'message': 'no audits yet', 'last_updated': now_iso}, indent=2))
    else:
        try:
            s = json.loads(AUDIT_STATUS_PATH.read_text())
            s['last_updated'] = now_iso
            AUDIT_STATUS_PATH.write_text(json.dumps(s, indent=2))
        except Exception:
            AUDIT_STATUS_PATH.write_text(json.dumps({'message': 'no audits yet', 'last_updated': now_iso}, indent=2))


if __name__ == '__main__':
    main()
