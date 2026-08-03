# Tokenomics — $BOTTT & PIXEL

## $BOTTT (name `LPC-BOT`, symbol `BOTTT`)

| | |
|---|---|
| Address | `0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75` (Ethereum) |
| Standard | ERC‑20 · 18 decimals · supply 1,000,000,000 |
| Permit | **EIP‑2612 ✓** · EIP‑3009 ✗ |
| Type | Uniswap **V4** token (transfer‑gated) with buyback |

### ⚠️ $BOTTT is non‑transferable peer‑to‑peer

The token's `_afterTokenTransfer` hook **reverts (`InvalidTransfer`)** for any transfer that isn't a mint, burn, pool (Uniswap V4 `poolManager`), factory, or distributor. A per‑transaction "transfer allowance" lives in **transient storage** and only the V4 hook can raise it (during swaps).

**Consequences:**
- You **cannot** `transfer`/`transferFrom` $BOTTT wallet‑to‑wallet.
- You **can** buy/sell it on the pool, and **hold** it.
- So **x402 per‑call payment in $BOTTT is not possible** — the transfer would revert.

### The model: hold‑to‑access

Because holding works (`balanceOf`) but sending doesn't, the paid agents use **hold‑to‑access**:

| Agent | Requirement |
|---|---|
| 🧭 Collector Tutor | free — hold **any** ecosystem NFT |
| 🎨 Pixel‑Art Generator | hold **≥ 100,000 $BOTTT** or any ecosystem NFT |
| 🧱 Voxel Architect | hold **≥ 200,000 $BOTTT** or any ecosystem NFT |

Demand comes from users **buying and holding** $BOTTT to unlock the agents; the token's built‑in **buyback** captures value. No per‑call transfer needed.

> If a per‑call **USD** micro‑fee is ever desired, use a freely‑transferable stablecoin (USDC) via x402 — $BOTTT stays the access/utility token.

Acquire $BOTTT: https://www.tenthousandtokens.net/browse/0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75

## PIXEL (the fungible resource)

- Lives inside **Resources (LPGR)** `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548` as the fungible token you **burn to mint**.
- Earned **free** from the weekly **Streaming Pixels** faucet (`SPIXELS` `0xeBD9…A5f1`, random 1–11, holder‑gated, weekly epochs).
- Minting pixel‑art in **LPLART** costs `0.0001 ETH` + burns `1 PIXEL`.
