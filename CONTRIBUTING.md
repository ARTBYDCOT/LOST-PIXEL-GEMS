# Contributing to Lost Pixel Gems

Lost Pixel Gems is **open public art and open code**. This repository is deliberately **open to audits and to code contribution** — especially for **developing and hardening the on-chain contracts** (PIXELS token, voxel-LAND mint, on-chain map archive).

Art is by **D.C.O.T. and anyone who contributes.** The same spirit applies to the code.

## Ways to contribute

| Track | What | Where |
|---|---|---|
| **Contracts** | Design/implement/audit the PIXELS burn-to-mint, LAND, and on-chain voxel archive contracts | `contracts/`, [documentation/lost-pixel-gems-docs/docs/02-conceptos/CONTRACTS.md](documentation/lost-pixel-gems-docs/docs/02-conceptos/CONTRACTS.md) |
| **Security audits** | Review contracts & the map API for vulnerabilities | see [SECURITY.md](SECURITY.md) |
| **Apps / tools** | Editor, viewers, map, UX, mobile | `web/` |
| **Docs / economy** | Refine the deflationary model, tables, diagrams | `documentation/` |
| **Art pipeline** | `.vox` → optimized web meshes | [documentation/lost-pixel-gems-docs/docs/04-recursos/ASSETS.md](documentation/lost-pixel-gems-docs/docs/04-recursos/ASSETS.md) |

## On-chain contract development (priority)

The economy in [documentation/lost-pixel-gems-docs/docs/02-conceptos/ECONOMY.md](documentation/lost-pixel-gems-docs/docs/02-conceptos/ECONOMY.md) is a **framework awaiting deployed contracts**. We welcome PRs and audits for:

1. **PIXELS (ERC-20)** — fixed supply, no post-genesis emission, burnable.
2. **Voxel-LAND mint** — `mintVoxel(bytes voxelData) payable` style: **burns PIXELS ∝ voxel count**, mints the model NFT, records position.
3. **On-chain map archive** — stores kept blocks + metadata so the map is **rebuildable from contract data alone** (server-independent).
4. **Read-only exhibition** — a 6-word *signed* message grants *view-only* display of a wallet's NFTs; **never** a transfer/approval.

**Ground rules for contract PRs**
- Include tests (Foundry/Hardhat) and a short threat model.
- No hidden mint/withdraw/owner backdoors — this is public art infrastructure.
- Deflation must be **structural**: no faucet, no inflationary emission.
- Prefer minimal, auditable code over cleverness.

## How to open a PR
1. Fork → branch (`feat/…`, `contracts/…`, `audit/…`).
2. Keep it scoped; describe the *why*.
3. For contracts: attach test output + gas notes.
4. **Never commit** private data, keys, `.env`, databases, or wallet material.

## Code of conduct
Be constructive. This is a commons — build like others will build on top of you.
