ABI Upload Templates

This folder contains templates and an example ABI file format for auditors to upload verified ABIs into /contracts.

Naming convention:
- Filename: <checksummed-address>.abi.json (example: 0xAbC123...Def.abi.json)
- Place the file at the repository root path: /contracts (do NOT put ABIs under unrelated subfolders).

Required JSON schema (machine-friendly):
{
  "address": "0x...",
  "chainId": 1,
  "name": "ContractName",
  "verified_on": "2026-08-07T00:00:00Z",
  "source_url": "https://etherscan.io/address/0x...#code",
  "abi": [ /* ABI array */ ]
}

Example file is provided as example.abi.json in this folder.

Upload guidance:
- Verify ABI matches the verified source (Etherscan or similar) before committing.
- Use checksummed address in the filename to avoid collisions.
- Include a link to the verification page in source_url.
- Keep ABIs minimal (only the ABI array + required metadata) and valid JSON.
