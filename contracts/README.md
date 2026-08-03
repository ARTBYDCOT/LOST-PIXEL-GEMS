Contracts ABIs for auditors

Purpose
This folder is the canonical place to publish verified contract ABIs for auditors and tooling. Place each verified ABI as a separate JSON file so auditors can quickly import into their analysis tools.

File naming convention
- Use checksummed address as the filename, lowercase with 0x prefix: 0xabcdef... . Example: 0xa0795E3665552A1ea784e8e0d465A6E65455b51B.abi.json
- Optionally include symbol or friendly name: 0xa0795E3__LPGMA.abi.json
- Always use .abi.json extension.

ABI file schema (recommended)
{
  "address": "0x...",
  "chainId": 1,
  "name": "Contract Name",
  "symbol": "SYM",
  "verified_on": "2026-08-03T12:00:00Z",
  "source_url": "https://etherscan.io/address/...#code",
  "abi": [ ... ]
}

Quality guidance
- Prefer verified on-chain source (Etherscan/Basescan) and include source_url.
- Include chainId (1 for mainnet) to avoid confusion.
- Keep ABIs minimal (the JSON ABI array) but include the wrapper metadata above.

Uploading process
- Add ABI files under this directory and open a PR, or open an issue linking the file and request maintainers to merge.
- For sensitive or private review-only ABIs, use a private channel (Security Advisory) — do NOT commit private ABIs to the public repo.

Notes
- The refresh-audit workflow reads documentation/lost-pixel-gems-docs/contracts.json. ABIs here are for auditors and do not replace the registry file.
- If you want help importing ABIs in bulk, open an issue and tag maintainers.
