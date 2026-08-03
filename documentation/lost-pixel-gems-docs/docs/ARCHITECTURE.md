# Architecture

```
                          ┌──────────────────────────────────────────┐
   User / wallet  ─────►  │  Front‑ends (host‑agnostic, static)       │
                          │  lpc-bot.art · lostpixelgems.space        │
                          │  home chat · studios · maps · galleries   │
                          └───────┬───────────────────────┬──────────┘
             (relative/CORS fetch)│                       │ (ethers v6 · wallet)
                          ┌───────▼──────────┐    ┌────────▼────────────────┐
                          │ Agent gateway    │    │  Ethereum L1 / Base L2  │
                          │ (Node, ERC‑8257) │    │  contracts (see docs)   │
                          │ /api/* + /.well‑ │    │  · collections (SVG/    │
                          │  known/ai‑tool/* │    │    voxel on‑chain)      │
                          │ holder/hold gate │◄───┤  · $BOTTT, PIXEL        │
                          └───────┬──────────┘RPC │  · ERC‑8257 registry    │
                                  │ resolves       │    0x265BB2…2cf1        │
                          ┌───────▼──────────┐    └─────────────────────────┘
                          │ Resolver relayer │
                          │ tokenURI/holdings│
                          │ (Blockscout+RPC) │
                          └──────────────────┘
```

## Principles

- **Fully on‑chain art.** SVG (pixel) and voxel data live in the contracts. Front‑ends **read galleries directly from chain** (via `tokenURI`) and are **host‑agnostic** — the same site works on emblem, Hostinger, or IPFS. Never ship a manual `.htaccess`.
- **No secrets in the browser.** Any tokens/keys are server‑side in the gateway. All signing is user‑side (MetaMask).
- **Agents = ERC‑8257 tools.** The gateway hosts manifests + endpoints; the registry stores URI + hash on‑chain; OpenSea indexes them permissionlessly.
- **Gating is on‑chain reads.** Holder gate (Tutor) and hold‑to‑access (paid) are `balanceOf` checks, cached, multi‑chain.
- **Self‑mint.** Creative agents generate + hand off to the studios; the **user mints** (keeps their own gas), rather than a custodial bot minting.

## Components in this repo's world

| Component | Where |
|---|---|
| Character portal + agent UI | `lpc-bot.art` (static) |
| Ecosystem app (city, studios, maps, galleries) | `lostpixelgems.space` (static) |
| Agent gateway (ERC‑8257) | Node server (emblem → `agent.lpc-bot.art`) |
| Resolver relayer | Node server |
| On‑chain state | Ethereum + Base contracts (see [CONTRACTS.md](./CONTRACTS.md)) |

## Standards

- **ERC‑721 / ERC‑1155** — collections & faucet.
- **ERC‑20 + EIP‑2612** — $BOTTT.
- **ERC‑8257** — Agent Tool Registry (the agents).
- **x402** — payment negotiation (advertised; $BOTTT uses hold‑to‑access instead of transfer).
- **CC0 1.0** — license.
