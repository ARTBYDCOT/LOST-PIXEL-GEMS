<div align="center">

# 🟢 Lost Pixel Gems — Ecosystem & On‑Chain AI Agents

**A fully on‑chain pixel‑art / voxel NFT universe by [D.C.O.T.](https://www.dcot.space) — with a 3‑in‑1 on‑chain AI agent (LPC‑BOT) built on OpenSea's ERC‑8257 tool standard.**

`lpc-bot.art` · `lostpixelgems.space` · CC0

</div>

---

## What this is

Lost Pixel Gems is a multi‑collection on‑chain ecosystem: pixel‑art gems, editable voxel LAND, an open art gallery (LPLART), a fungible resource (PIXEL), a physical PhyGital line, and cross‑chain (Ethereum + Base) collections. On top of it runs **LPC‑BOT**, an **on‑chain AI agent** — *3 agents in 1 character* — registered as **ERC‑8257 tools** and payable/gated in **$BOTTT**.

- **Everything is fully on‑chain** (SVG/voxel data lives in the contracts; the front‑ends are host‑agnostic and read galleries directly from Ethereum/Base).
- **The agents** are discoverable on the OpenSea Agent Tool Registry and callable from any agent framework.
- **Everything here is CC0** — see [LICENSE](./LICENSE).

## Documentation map

| Doc | What's inside |
|---|---|
| [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) | How the pieces fit: contracts ↔ front‑ends ↔ agent gateway ↔ registry. |
| [docs/CONTRACTS.md](./docs/CONTRACTS.md) | **Every contract** in the ecosystem — address, chain, standard, purpose, key functions, ABIs. |
| [docs/AGENTS.md](./docs/AGENTS.md) | The **LPC‑BOT agents** (ERC‑8257 tools 114 & 115): manifests, endpoints, access model, x402/hold‑to‑access, IP. |
| [docs/WALLET.md](./docs/WALLET.md) | **Wallet connection & signing** — connect, chain switching, mint, approve/burn PIXEL, registerTool / updateToolMetadata, holder gates. |
| [docs/TUTORIALS.md](./docs/TUTORIALS.md) | Step‑by‑step: use the agents, mint pixel‑art, build voxel, register a tool on‑chain, verify on OpenSea. |
| [docs/API.md](./docs/API.md) | The agent gateway HTTP API (`/api/*`, `/.well-known/ai-tool/*`) and the on‑chain resolver relayer. |
| [docs/TOKENOMICS.md](./docs/TOKENOMICS.md) | $BOTTT, PIXEL, the hold‑to‑access model, and why per‑call transfer is disabled. |
| [LICENSE](./LICENSE) | CC0 1.0 Universal — public domain dedication. |

## Quick facts

- **Networks:** Ethereum mainnet (chain `1`) + Base (chain `8453`).
- **Agent registry (ERC‑8257):** `0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1` (Ethereum + Base).
- **Fee/utility token — $BOTTT (name `LPC-BOT`, symbol `BOTTT`):** `0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75` (Ethereum, 18 dec).
- **Character / IP collection — LPC‑BOT (ERC‑721):** `0x3560dc18d27888de170acbc119442db3fdcf5ccf` (111 on‑chain BOTs, identity token **#100**).
- **Live agents:** `toolId 114` Collector Tutor (free · holder‑gated) · `toolId 115` Pixel‑Art Generator (hold‑to‑access $BOTTT).

## License

Everything in this repository and every contract listed here is released under **CC0 1.0** (public domain). No rights reserved. Attribution appreciated but not required.
