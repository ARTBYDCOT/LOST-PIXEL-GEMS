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
