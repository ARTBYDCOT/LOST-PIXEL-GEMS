# LPC‑BOT Agents — ERC‑8257 tools

LPC‑BOT is **3 agents in 1 character**, built on OpenSea's **ERC‑8257 Agent Tool Registry** + **x402** payment negotiation. Its on‑chain **identity/IP is the LPC‑BOT ERC‑721 collection** (`0x3560…5ccf`, identity token **#100**).

## Registry

| | |
|---|---|
| **Registry contract** | `0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1` (Ethereum + Base) |
| **ERC‑8257 spec** | https://eips.ethereum.org/EIPS/eip-8257 |
| **Creator wallet** | `0x843819E77947e2Ca4F198dFa9c32cF49b598EF4B` |
| **Gateway (endpoint host)** | `https://build-3150f75ad03f2c47095fd160.emblem.build/pub/web_development/lpc-agent` *(moving to `agent.lpc-bot.art`)* |

## The three agents

### 🧭 Collector Tutor — `toolId 114` · FREE
- **Function:** ecosystem tour, multi‑chain tracking, collection info, **BOT traits & rarity** (e.g. "rarest traits", "traits of #7", "which bots have ZOMBIE BOT"), and buy/invest/collect guidance.
- **Access:** **free but holder‑gated** — hold **any** ecosystem L1 ERC‑721 (GEMS V1/V2, VOX LAND, Resources, LPC‑BOT, ABS, Assets, LPLART, THE LOST PIXEL GEM) **or any Travelers/Habitantes** collection (Base+ETH). Enforced server‑side (`402` if not a holder). Predicate hint: `IERC721Holding` (kind `0xbdf8c428`, logic OR).
- **Endpoint:** `POST /api/tools/collector-tutor` — `{ "message": string, "wallet": "0x..." }` → `{ reply, owner }`.

### 🎨 Pixel‑Art Generator — `toolId 115` · hold‑to‑access
- **Function:** describe a piece (or a photo) → generates pixel‑art (Pollinations engine) → hands off to **Lost Pixel Studio** → you **mint it yourself** on‑chain into **LPLART** (self‑mint keeps your gas in your control).
- **Access:** **hold‑to‑access** — hold **≥ 100,000 $BOTTT** *or* any ecosystem NFT. (`$BOTTT` is non‑transferable P2P, so access is by **holding**, not per‑call transfer — see [TOKENOMICS](./TOKENOMICS.md).)
- **Endpoint:** `POST /api/tools/pixel-art-mint` — `{ "prompt": string, "wallet": "0x..." }` → `{ access, studio, art, reply }`.

### 🧱 Voxel Architect — *in training*
- **Function:** turn a 2D idea into a **100% voxel (block)** model (≤ 250³), playable on the Lost Pixel maps; delivered in **Voxel Studio** for you to mint on your LAND.
- **Access:** hold‑to‑access **≥ 200,000 $BOTTT** or an ecosystem NFT. Not yet registered on‑chain (knowledge base being fed with architecture/urbanism references).

## Manifest (ERC‑8257 v1)

Each tool serves a canonical JSON manifest at `/.well-known/ai-tool/<slug>.json` on the gateway origin; its `keccak256` (JCS‑canonicalized) is committed on‑chain as `manifestHash`.

```jsonc
{
  "type": "https://ercs.ethereum.org/ERCS/erc-8257#tool-manifest-v1",
  "name": "collector-tutor",
  "description": "Free collector tutoring … · IP: the LPC-BOT collection (opensea.io/collection/lpc-bot), identity BOT #100. Use at https://lpc-bot.art · Ecosystem: https://lostpixelgems.space",
  "endpoint": "https://…/lpc-agent/api/tools/collector-tutor",
  "inputs":  { "type":"object", "properties": { "message": {"type":"string"}, "wallet": {"type":"string"} }, "required": ["message"] },
  "outputs": { "type":"object", "properties": { "reply": {"type":"string"}, "owner": {"type":"boolean"} } },
  "version": "1.0.0",
  "image": "https://…/lpc-bot-art/collection/images/100.svg",   // 1:1 on-chain BOT #100
  "externalUrl": "https://lpc-bot.art",
  "tags": ["nft","ai","trading","lost-pixel"],
  "creatorAddress": "0x843819…ef4b",
  "access": { "logic":"OR", "requirements":[{ "kind":"0xbdf8c428", "data":"0x…3560…", "label":"Hold any Lost Pixel ecosystem ERC-721" }] },
  "io.lostpixel.ipCollection": { "chainId":1, "address":"0x3560…5ccf", "name":"LPC-BOT", "identityTokenId":100, "opensea":"https://opensea.io/collection/lpc-bot" },
  "io.lostpixel.app": "https://lpc-bot.art",
  "io.lostpixel.ecosystem": "https://lostpixelgems.space"
}
```

Paid tools (Pixel/Voxel) carry an `access` block requiring a **$BOTTT holding** (custom kind `0x00000020` with the token address in `data`), **not** a `pricing` entry — because $BOTTT cannot be transferred per call.

## Discovery

- On‑chain registry crawl (permissionless) → indexed by OpenSea at **opensea.io/tools**.
- Gateway discovery: `GET /api/tools`, `GET /.well-known/ai-tool` (list), `GET /.well-known/ai-tool/<slug>.json`.
- OpenSea API/CLI/MCP:
  ```bash
  opensea tools get ethereum 0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1 114
  curl "https://api.opensea.io/api/v2/tools/ethereum/0x265BB2…/115" -H "x-api-key: KEY"
  ```

## Registering / updating a tool (on‑chain)

The creator wallet signs `registerTool` / `updateToolMetadata`. See [WALLET.md](./WALLET.md) for the full ethers v6 flow and the browser deploy console (`deploy-tools.html`).

```
registerTool(metadataURI, manifestHash, accessPredicate=0x0) → toolId
updateToolMetadata(toolId, newURI, newHash)
```
`accessPredicate = 0x0` (open on the registry) → the holder/hold‑to‑access gate is enforced by the agent server. A dedicated `IERC721Holding`/ERC‑20 predicate can be deployed later for fully on‑chain gating.
