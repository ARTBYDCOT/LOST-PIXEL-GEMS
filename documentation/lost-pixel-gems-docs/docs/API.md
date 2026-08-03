# Agent gateway API

The LPC‑BOT gateway is a small Node HTTP server (no framework, no DB). It hosts the ERC‑8257 manifests, the tool endpoints, the on‑chain holder/hold gates, and read helpers. **CORS `*`** (public read).

Base: `https://build-3150f75ad03f2c47095fd160.emblem.build/pub/web_development/lpc-agent` *(→ `agent.lpc-bot.art` once the domain is on Cloudflare)*.

## Discovery & manifests (ERC‑8257)

| Method · Path | Returns |
|---|---|
| `GET /api/tools` | list of tools `{ slug, manifest, name, paid, gated }` |
| `GET /.well-known/ai-tool` | `{ tools: [slug…] }` |
| `GET /.well-known/ai-tool/<slug>.json` | the v1 manifest (hashed on‑chain) |

## Tool endpoints

| Method · Path | Body → Returns |
|---|---|
| `POST /api/tools/collector-tutor` | `{ message, wallet }` → `{ reply, owner }` · `402` if not a holder |
| `POST /api/tools/pixel-art-mint` | `{ prompt, wallet }` → `{ access, studio, art, reply }` · gated by $BOTTT holding |
| `POST /api/tools/voxel-architect` | `{ prompt, dims, wallet }` → `{ access, studio, reply }` |
| `GET  /api/tools/<slug>` | friendly JSON (endpoints are POST‑only) |

## Read helpers (used by the front‑ends)

| Method · Path | Returns |
|---|---|
| `GET /api/health` | `{ ok, agents, collections, brain }` |
| `GET /api/collections` | the ecosystem registry (collections + agents + fee token) |
| `GET /api/owns?address=0x…` | `{ owner, hits:[{sym,count}] }` — multi‑chain ownership across all ecosystem + Travelers collections (cached 3 min) |
| `GET /api/estimate` | live cost/market estimate (gas, $BOTTT, fees) |
| `GET /api/market` | `{ ethUsd, bottt, pixelFee, gemsV1 }` (live ETH price) |
| `GET /api/pricing` | pricing/access config |
| `POST /api/chat` | `{ message, agent, wallet }` → grounded/LLM reply; guide is holder‑gated, creative agents are hold‑to‑access |

## On‑chain resolver relayer

A companion service resolves NFT metadata/images (including on‑chain SVG and CryptoPunks) and multi‑chain holdings via Blockscout + `tokenURI` fallback.

Base: `…/pub/web_development/roulette-relayer`

| Path | Returns |
|---|---|
| `GET /nft?chainId=&token=&id=` | `{ image, name, description, attributes }` (on‑chain metadata) |
| `GET /holdings?chainId=&address=` | wallet holdings |
| `GET /collection?chainId=&token=&max=` | collection items |

## Resilience

All front‑end clients parse responses defensively (`sj()` — text → `JSON.parse`, otherwise "server busy — try again") so a restarting gateway never crashes the UI.
