# Tutorials

Step‑by‑step guides for users, collectors and developers.

## A. Use the free Collector Tutor (holders)

1. Open **https://lpc-bot.art** — the AI chat is always open on the home page (or tap **◆ AI**).
2. Click **Connect wallet** and approve.
3. If you hold **any** ecosystem NFT (or a Traveler) → tutoring unlocks, free.
4. Ask things like:
   - *"Give me a tour of the ecosystem"*
   - *"What is THE LOST PIXEL GEM and how do I buy?"*
   - *"rarest traits"* · *"traits of #7"* · *"which bots have ZOMBIE BOT"*

## B. Generate & mint pixel‑art (Pixel‑Art agent)

1. On lpc-bot.art, switch to the **🎨 Pixel‑Art** agent.
2. Ensure access: hold **≥ 100,000 $BOTTT** or any ecosystem NFT.
3. Describe your art (or upload a photo). The agent generates it and gives you a **Lost Pixel Studio** link.
4. In the Studio the art auto‑draws; tweak it, then hit **🏛 Mint** → it mints on‑chain into **LPLART** (`0.0001 ETH` + burns `1 PIXEL`).
   - Need PIXEL? Claim free from the weekly **Streaming Pixels** faucet.

## C. Build voxel (Voxel Architect — in training)

1. Switch to the **🧱 Voxel** agent (hold ≥ 200,000 $BOTTT or an ecosystem NFT).
2. Describe the build (e.g. "art‑deco gallery house", ≤ 250³).
3. The agent delivers a model in **Voxel Studio**; edit it in 3D and **mint it yourself** onto your **LOST PIXEL VOX LAND** parcel.

## D. Register an agent as an ERC‑8257 tool (developers)

1. Build a manifest (see [AGENTS.md](./AGENTS.md)) and serve it at `/.well-known/ai-tool/<slug>.json` on the same origin as its `endpoint`.
2. Compute `manifestHash = keccak256(JCS(manifest))`.
3. From the creator wallet, call `registerTool(metadataURI, manifestHash, 0x0)` on the registry `0x265BB2…2cf1`.
4. Read `toolId` from the `ToolRegistered` event.
5. To change metadata later: `updateToolMetadata(toolId, uri, newHash)`.

> Use the bundled **`deploy-tools.html`** console: connect wallet → Register / Update with a click.

## E. Verify your tool on OpenSea

1. OpenSea's registry indexer crawls the on‑chain registry automatically (minutes–hours).
2. Find it at **opensea.io/tools** (search "LPC‑BOT") or query:
   ```bash
   opensea tools get ethereum 0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1 114
   ```
3. Requirements for a clean listing: manifest reachable, `manifestHash` matches, `image` is 1:1, endpoint responds.

## F. Get $BOTTT (hold‑to‑access)

$BOTTT is **non‑transferable P2P** — you can't send it wallet‑to‑wallet; you **buy and hold** it. Get it via the pool: **https://www.tenthousandtokens.net/browse/0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75**. Holding ≥ the agent's threshold unlocks that agent.
