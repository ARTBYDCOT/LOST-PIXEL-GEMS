# Lost Pixel — Ecosystem Update

> Date: 2026-11-06
> Owner / deployer: `dcot-deployer.eth` = `0x843819E77947e2Ca4F198dFa9c32cF49b598EF4B`
> Burn sink: `0x…dEaD`

## 1. The three properties (one creative ecosystem)

| Domain | Role | Stack |
|---|---|---|
| **lostpixelgems.space** | Creative engine and on-chain galleries. Voxel Editor, Pixel Studio, Playground, Genome Bridge, Gene Explorer, Explorer, City Live, Data Hub, Collections. | Static HTML/JS + PHP on Hostinger |
| **lostpixelgems.fun** | $LPCG playground and mutation lab. Entry point for the LPCG warriors and community mutations. | Hostinger |
| **lpc-bot.art** | Agent layer. The 111-bot network, collective brain, ERC-8257 agent tools, agent registry, world builder, ecosystem mind-map. | Hostinger + Emblem build artifacts |

### Creative loop
- Access-key economy: own **GEM V1 #N** → free **CLAIM LAND #N** (LPVL). Build the parcel in the Voxel Editor → persist 100% on-chain.
- **PIXELS (LPGR, ERC-1155 #2)** are the deflationary fuel burned to craft pixel and voxel art, mint, and place assets on the map.
- **Genome Bridge** exposes LPCG traits and 2D/3D voxel art as a public CC0 API; the Voxel Editor remains the single source of truth.
- Agents know and act across the full ecosystem through the brain; each is an ERC-8257 tool with a machine endpoint and human direct-chat page.

---

## 2. Contracts & addresses

### Ethereum L1

| Collection | Symbol | Type | Address | Notes |
|---|---|---|---|---|
| LOST PIXEL GEMS V1 | LPG | ERC-721 | `0xb52cD7A93878D823dF0fBc4F2E5a42f7b5B53A44` | Access key — 111 original on-chain gems. |
| LOST PIXEL GEMS V2 | LPGNTRCTV | ERC-721 | `0xb8698f54BEAd61D0C34e60Ab49d5AC992674f01B` | Interactive gems. |
| LOST PIXEL VOX LAND | LPVL | ERC-721 | `0x75C3952A1CE57D259A5A66b57c3cae61C14bae52` | Canonical lands. Deprecated `0x52B0…4757` is frozen. |
| LOST PIXEL GEMS RESOURCES / PIXELS | LPGR | ERC-1155 (#2) | `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548` | Deflationary fuel. |
| LPC-BOT | BOTTT | ERC-721 | `0x3560dc18d27888de170acbc119442db3fdcf5ccf` | 111 BOT IP slots, contract renounced. |
| LOST PIXEL GEMS ASSETS | LPGA | ERC-721 | `0xa0795E3665552A1ea784e8e0d465A6E65455b51B` | On-chain VOX models. |
| VOXEL MAP · Genesis Map 1 | MAP | Protocol | `0x513493926EedeE69B6a8d65a1068CFa87855dad3` | Public on-chain voxel map. |
| LOSTPIXELPOOL | LPP | ERC-20 / 721 pool | `0xF364c3F723C98dB51679a44e2871367Ce630FCfF` | Claims pool. |
| STREAMING PIXELS | SPIXELS | ERC-1155 faucet | `0xeBD9ab3fbFB38F8db0C7caaC343382bae08FA5f1` | Weekly free PIXELS. |
| LOST PIXEL LEGACY | LPLART | ERC-721 | `0x84198807972F196ED7D8b18B3B7A55B14237C0ea` | Community mint. |
| THE LOST PIXEL GEM | GEM | ERC-721 | `0x1214f9dC859cD1495607a6188B2d4050e5bc287b` | 10,000-gem collection. |
| PIXELGEMS (POOLGEMS) | PIXELGEMS | ERC-721 | `0x3970435717de610087D7dA9203aA145580655388` | On-chain pixelgems. |

### Base (8453)

| Collection | Address | Notes |
|---|---|---|
| LOST PIXEL CITY TRAVELERS | `0xdc9430d36a30dfd732c16c63238b31c5a84fd98e` | Main Base collection. |
| LOST PIXEL CITY RESIDENTS | `0x718eb4067ea4c8f0eae0b7f7beeaeef463b73d4f` |  |
| Mutant Lost Pixel City | `0xb458397525ac01fc4b4a2fca8470121621c21c66` |  |
| RE-BURN LPC | `0xe9043dd09da79c23307613655fce2003191e9b18` |  |
| LPGBA | `0x77e95Bd2098BE1e75a1C36272b1e255F68358522` | Mint 100% on-chain. |
| ERC-8257 Tool Registry | `0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1` | Agent tools live here. |

### Robinhood Chain (4663)

| Collection | Address | Notes |
|---|---|---|
| LPCG | `0x305c539894622a52f4176252208f28459898d6d9` | 11,104 chess-warriors. CC0. |
| LPCG MEMES | `0x925eb67d6003ab817ece303757f9490ac7c4ba41` | Holder-gated meme drops. |
| LPCG BATTLES | `0x4d0552984A34F32B04CC6AF8A58399D21be837Ab` | Chess-battle 1/1s. |

---

## 3. What to keep updated across the repo

1. Replace stale contract addresses with the canonical tables above.
2. Flag deprecated `LPVL 0x52B0…4757` and lands extension `0x168d…1189` as frozen/deprecated.
3. Keep the `.space` / `.fun` / `lpc-bot.art` links connected through the shared nav concept.
4. Document the machine endpoint split: `tool.php?agent=N` (POST, machine) vs `tool.html?agent=N` (human chat)
5. Note the single source of truth for voxel heads: `/api/token-head`.

---

## 4. Release notes / 2026-11-06 highlights

- City-live world and genome↔editor↔playground head sync.
- Agent audit cards and ops-control tooling.
- Tool manifest flow with dual `.php` and `.html` links.
- Gemini-first image routing with billing guardrails.
- Shared nav.js overhaul (Maps / Collections / Ecosystem / Community). 

This documentation is the public reference copy for the current Lost Pixel ecosystem and should remain aligned with the contract registry and collections pages.
