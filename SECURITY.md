# Security & Audits

This project is **open to security audits**. The protocol contracts (PIXELS,
VoxelLAND, MapArchive, Exhibition) are meant to be reviewed in the open before
mainnet deployment.

## Reporting
- Non-sensitive: open an issue or an `audit/…` PR.
- Sensitive/exploitable: open a private GitHub Security Advisory.

## Scope
- Smart contracts in `contracts/` (highest priority).
- The public-map API (`server/node`, `server/php`) — input validation, owner-gating.
- Client wallet flows (read-only calls, signed messages).

## Non-negotiables (by design)
- No hidden mint / withdraw / owner backdoors.
- Deflation is structural: no faucet, no post-genesis emission.
- The read-only Exhibition never transfers or approves NFTs.

## Audit Requests

This project welcomes public and coordinated Web3 security audits. To request an audit, please use the provided GitHub issue template ("Audit Request") so requests are structured and actionable.

How to request an audit (public):
1. Open a new issue using the "Audit Request" template: .github/ISSUE_TEMPLATE/audit_request.md
2. Include: contract path(s), deployed address(es) with verification links, ABI/solidity sources, scope (full audit / gas review / integration), and desired timeline.
3. Set disclosure preference: Public report, Coordinated disclosure, or Private advisory.
4. For high-severity or exploitable issues, open a private GitHub Security Advisory instead of a public issue.

Triage & response: The maintainers aim to acknowledge new audit requests within 72 hours and provide an initial triage. For sensitive advisories the security team will respond privately and coordinate disclosure.

Contact for coordinated disclosure: open a Security Advisory or DM the repository maintainers via GitHub.

Labels: 'audit-request' and 'security' will be applied to audit issues automatically when using the template.

For more details see: .github/ISSUE_TEMPLATE/audit_request.md
