# ABI upload

Use this template when submitting a PR that adds or updates a verified ABI under /contracts.

Title format: "Add verified ABI: <ContractName> (0x<address>)"

Body checklist (required):
- [ ] ABI file added to /contracts named exactly: `<checksummed-address>.abi.json`
- [ ] ABI JSON includes the following top-level fields: `address`, `chainId`, `name`, `verified_on` (ISO8601), `source_url`, `abi` (array)
- [ ] `source_url` links to the verified source page (Etherscan, Blockscan, or equivalent)
- [ ] ABI validated locally (e.g., `python -c "import json; json.load(open('path'))"`)
- [ ] Brief explanation of the verification steps taken (which explorer, date, and any notes)

Maintainer notes:
- Repository CI may run a lightweight JSON schema check. If it fails, ask contributor to fix formatting.
- Do not merge without at least one maintainer review confirming the `source_url` matches the contract address.

Thank you for contributing a verified ABI.