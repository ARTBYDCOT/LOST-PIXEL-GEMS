# THE LOST PIXEL GEM — Protocol (10K NFT SIDE PROJECT)

**A fully on‑chain, deflationary, rewritable NFT ecosystem on Ethereum L1.**
Burn your original gem → mint the same token as a **100% on‑chain** version → sculpt it, fuse it, and grow it over time. Every image, trait and animation lives in the contract itself — no IPFS, no servers, no external art.

by **DCOT**

---

## 1. Distribution & Timeline

| Phase | What happens |
|------|---------------|
| **Aug 14, 2026 — FREE MINT** | The original collection (10,000 gems) is a **free mint on OpenSea**. Anyone can mint. |
| **Open market + accumulation** | Secondary trading opens. Collectors buy, sell and accumulate gems freely. |
| **+1 week after market open — THE BURN OPENS** | The migration app goes live. Holders **burn** their original gem and **claim** the new 100% on‑chain version (same token id). |

> The burn is permissionless and permanent. You are not required to migrate — but only migrated gems become fully on‑chain, rewritable, and eligible for fusion, the PIXELS economy and the auction house.

---

## 2. The Claim (Burn → Mint)

When you claim, in **one transaction** you:

1. **Burn** your original gem (ERC‑721, metadata on IPFS) — sent to `0x…dEaD`, gone forever.
2. **Mint** the new **PIXELGEMS** token with the **same id** — its art, traits and animation are generated 100% on‑chain from a ~201‑byte record (SSTORE2), Merkle‑verified against the collection root.
3. **Receive 6 PIXELS** — every one of the 10,000 gems grants **6 PIXELS per wallet** on claim (flat, once per wallet).

The claim is signature‑gated (EIP‑712) by a dedicated backend signer, ownership‑verified on‑chain per token, and replay‑protected with a per‑wallet nonce. **You pay only your own gas.**

---

## 3. Contracts (Ethereum Mainnet)

| Contract | Address |
|---------|---------|
| **PIXELGEMS** — the NFT (100% on‑chain, rewritable) | `0x3970435717de610087D7dA9203aA145580655388` |
| **POOLGEMS** — burn / claim controller + reward pool | `0x74b3AEA764A7a51a0BC20E031C46eD93f9aDf51B` |
| **PIXELS** — ERC‑1155 utility token (id `#2`) | `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548` |
| **PixelsShop** — buy PIXELS with ETH | `0x1e029d8d9Ebb7d8C74b6482f1b4109eEa872E832` |
| **AuctionHouse** — 24h English auctions | `0xbf9ce508802ec90ebd32a9fd716a6e6b3cf34254` |
| **OLD collection** — burned on claim | `0x1214f9dC859cD1495607a6188B2d4050e5bc287b` |

### Project accounts

- **Deployer / Treasury** (deploys the contracts, funds the reward pool + shop stock, receives the **8% royalty**): **`0x843819E77947e2Ca4F198dFa9c32cF49b598EF4B`** (`dcot-deployer.eth`).
- **Backend signer** (only authorizes claims via EIP‑712 signatures; **holds no funds and cannot move anything**): `0x33906f0E9aF9f52eE68DDa2F250065C8110607C0`.

> **Gas:** every collector pays their **own** gas for claim / mutate / fuse / burn. The **Treasury `0x8438…EF4B`** funds the operations of the protocol: it seeded the reward pool (**60,000 PIXELS** = 10,000 wallets × 6) and the shop stock (**80,000 PIXELS**), and paid for every contract deployment.

---

## 4. PIXELS — the utility token

**PIXELS** (ERC‑1155, `0x6912…c548`, id `#2`) are the fuel of customization. **Each PIXEL = the right to place one more voxel (cube) anywhere on your gem’s canvas.**

- **Base price:** **0.000888 ETH per PIXEL** (from the on‑chain PixelsShop).
- **Buy:** pay ETH to the PixelsShop → PIXELS land in your wallet.
- **Burn into your gem:** call `burnPixels(tokenId, qty)` → the PIXELS are transferred to the NFT contract and **locked forever** (deflationary). Your gem’s **voxel capacity increases by `qty`**.
- **Claim reward:** the first claim per wallet grants **6 free PIXELS** (24 base voxels + burned PIXELS = your total capacity).

Capacity is enforced 100% on‑chain: you can never paint more voxels than `24 (base) + PIXELS you burned`, and never beyond the current Z‑depth ceiling.

---

## 5. The Z‑axis — fusion & depth

Every gem is a **voxel volume of `24 × 24 × Z`**. The face canvas is always 24×24; **Z (depth) grows only through fusion.**

| Level | Volume | How you get there |
|------|--------|-------------------|
| **Lv0** | 24 × 24 × 1 | A freshly claimed gem (1 layer). |
| **Lv1 … Lv8** | 24 × 24 × N | **Each gem you fuse adds +1 Z layer.** Its face stacks behind, front‑to‑back. |
| **Apex (Lv8)** | 24 × 24 × 8 | Fuse up to 8 gems into one base. |
| **MAX** | 24 × 24 × 16 | Merge **two Lv8 apexes** into the maximum container. |

**Fusion = the SUM.** When you fuse, the burned gems are destroyed, their **PIXELS capacity is added to your base**, and their faces are written into the new Z‑layers **on‑chain in the same flow** (fuse + write). You choose which face is the **front** (the 2D image the token shows); by default the newest layer sits on top. The real depth is read on‑chain (`_depth(id)`), so wallets, the 3D viewer and the metadata all agree.

Deeper gems cost more gas to write (bigger record) → depth is prestige, and burning gems is deflationary.

---

## 6. Adding PIXELS (growing your gem) — step by step

1. **Buy PIXELS** from the PixelsShop at **0.000888 ETH** each (or use your 6 claim PIXELS).
2. **Burn them into your gem** (`burnPixels`) → +1 voxel capacity per PIXEL, placeable anywhere.
3. **Sculpt** on the 24×24×Z canvas (paint / erase / shape tools).
4. **Write on‑chain** (`mutate`) → your voxels are stored in the token’s record. The image, `animation_url` and the `Voxels Painted` trait update **live** — the metadata is a view function, so every rewrite is reflected instantly on OpenSea and every explorer.

You (the owner) pay the gas for each write. The record is rewritable up to Lv8, then two apexes merge to MAX. **Everything you add is permanent and 100% on‑chain.**

---

## 7. Marketplace — AuctionHouse

An independent, on‑chain **English auction** house:

- **24h per lot**, **+5% minimum bid step**, **anti‑snipe** (a bid in the last 10 min extends +10 min).
- **Bid in ETH** (USDC also supported). The NFT is held in **escrow**; outbid bidders are refunded automatically.
- On settle, payment is split **directly**: **royalty → the artist** (EIP‑2981), **3% platform fee → the house (DCOT)**, **the rest → the seller**. No bids → the NFT returns to the seller.
- Allowlisted collections: LOST PIXEL LEGACY, LOST PIXEL GEMS ASSETS, and PIXELGEMS.

---

## 8. Deflation & the Value Pyramid

Scarcity is engineered by fire:

- **Burned‑to‑claim:** every migration burns an original gem forever.
- **PIXELS locked:** every PIXEL burned into a gem is removed from circulation permanently.
- **Sealed pools:** retired reward pools from earlier versions are sealed as permanent burn pools (their signers set to `0`, funds unreachable).
- **Fusion:** every fusion destroys gems to grow one.

Many Level‑0 gems sit at the base; a rare few reach Apex and MAX at the top.

---

## 9. Security model

- **100% on‑chain art** — the render can never break: the contract rejects any record too short to render (`_checkRec`), so a token’s image is guaranteed forever.
- **No‑rug pools** — the reward pool cannot be swept by the owner; funds only leave via genuine claims. Rescue functions are time‑locked far into the future.
- **Claim gate** — EIP‑712 signature from a dedicated signer (holds no funds), on‑chain ownership check per token, per‑wallet nonce, rate‑limited backend, and private per‑token records that are never web‑served.
- **Wallet‑agnostic** — the app supports every major wallet (EIP‑6963: MetaMask, Coinbase, Rabby, Trust, Brave, OKX…) plus mobile deep‑links and WalletConnect. Every transaction re‑verifies the network and account before signing.

---

*The Lost Pixel Gem — scarcity engineered by fire. Built 100% on‑chain. by DCOT.*
