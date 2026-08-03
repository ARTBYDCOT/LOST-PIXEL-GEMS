# Contracts — Lost Pixel Gems ecosystem

Every contract, its address, chain, standard, and purpose. **All CC0.**
Networks: **Ethereum mainnet** (`chainId 1`) and **Base** (`chainId 8453`).

> Verify any address on the block explorer before interacting. Explorers:
> Ethereum → https://etherscan.io/address/&lt;addr&gt; · Base → https://basescan.org/address/&lt;addr&gt;

---

## 1. Core collections (Ethereum L1)

| Name | Symbol | Standard | Address | Notes |
|---|---|---|---|---|
| **Lost Pixel Gems V1** | LPG | ERC‑721 | `0xb52cD7A93878D823dF0fBc4F2E5a42f7b5B53A44` | 111 fully on‑chain pixel‑art gems. Genesis. **Mint closed.** |
| **Lost Pixel Gems V2** | LPGNTRCTV | ERC‑721 | `0xb8698f54BEAd61D0C34e60Ab49d5AC992674f01B` | Interactive on‑chain gems (gen 2). |
| **Lost Pixel Vox Land** | LPVL | ERC‑721 (dNFT) | `0x75C3952A1CE57D259A5A66b57c3cae61C14bae52` | Editable voxel LAND parcels; scenes persist on‑chain. Canonical Lands contract. |
| **Lost Pixel Gems Resources** | LPGR | ERC‑721 (+ fungible PIXEL) | `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548` | Holds **PIXEL** (token #2) — the fungible resource burned to mint. Earned free from the weekly STREAMING PIXELS faucet. |
| **LPC‑BOT** (character / IP) | BOTTT | ERC‑721 | `0x3560dc18d27888de170acbc119442db3fdcf5ccf` | 111 fully on‑chain BOTs · 69 unique traits · ownership renounced (`0xdead`). **Identity token: #100.** Hosts the AI agents. |
| **ABS.tract series** | ABS | ERC‑721 | `0x848f15ba0a652b09438c9747e80304147d87aa0a` | Abstract art series by D.C.O.T. |
| **Lost Pixel Gems Assets** | LPGA | ERC‑721 | `0x50B4bb42cD9A2b981291b834dCba55Ec53b60a9b` | Fully on‑chain voxel assets that populate the city. |
| **Lost Pixel Legacy** | LPLART | ERC‑721 | `0x84198807972F196ED7D8b18B3B7A55B14237C0ea` | Open on‑chain art gallery; each creation auto‑indexes into the map. The Pixel‑Art agent mints here. |
| **THE LOST PIXEL GEM** (flagship) | GEM | ERC‑721 | `0x1214f9dc859cd1495607a6188b2d4050e5bc287b` | 10,000 gems · 4 rarities · **mint 2026‑08‑14**. |

## 2. Protocol / infrastructure (Ethereum L1)

| Name | Symbol | Standard | Address | Notes |
|---|---|---|---|---|
| **$BOTTT token** (fee/utility) | BOTTT (`name: LPC-BOT`) | ERC‑20 | `0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75` | 18 dec · supply 1,000,000,000 · **EIP‑2612 permit** ✓ · **NO EIP‑3009** · Uniswap V4 token, **transfer‑gated (hold‑to‑access)** + buyback. See [TOKENOMICS](./TOKENOMICS.md). |
| **Voxel Map · Genesis Map 1** | MAP | Protocol | `0x5134f5df64c2b62a70Bcb5A96e1B8Cbf6C6B7dad3` | On‑chain 1:1 voxel placement of the city. |
| **LostPixelPool** | LPP | ERC‑20/721 pool | `0xF364c3F723C98dB51679a44e2871367Ce630FCfF` | Claims pool (CSV allocations; admin `dcot-deployer.eth`). |
| **Streaming Pixels** | SPIXELS | ERC‑1155 faucet | `0xeBD9ab3fbFB38F8db0C7caaC343382bae08FA5f1` | Weekly PIXEL airdrop faucet (random 1–11, holder‑gated, weekly epochs). |
| **Lands Extension** (Manifold ext) | — | tokenURI ext | `0x168d4e05606d61f070dd7ccced9cc5a53a0d1189` | **Deprecated / superseded** by LPVL. |
| **Physical burn NFT** (PhyGital) | — | ERC‑721 (burn‑to‑claim) | `0xa02d8c83cac62f865f4f62ac0645b2be5a29b35f` | Burn to claim the physical collectible (via Manifold). |

## 3. Base L2 collections (`chainId 8453`)

| Name | Symbol | Standard | Address | Notes |
|---|---|---|---|---|
| **Lost Pixel Gems (Base)** | LPGBA | ERC‑721 | `0x77e95Bd2098BE1e75a1C36272b1e255F68358522` | Asset minted 100% on‑chain to your wallet on Base. |
| **Lost Pixel Gems Map 2 (Base)** | MAP2 | Protocol | `0xe2bf4C47DE9876b8e55e352A05362caA2e1437A7` | Base voxel placement (optional, 1 PIXEL voucher). |
| **NFT Claims Roulette · 721 (Base)** | — | ERC‑721 | `0x9ebbfaf556f60439b7728c3335e916ce515cc7ef` | Roulette claim pool (v2). |
| **NFT Claims Roulette · 1155 (Base)** | — | ERC‑1155 | `0x3e826375156bd45987599d3decd71508856dccb7` | Roulette claim pool (v2). |

## 4. Travelers / Habitantes (Base + Ethereum)

The Travelers sub‑ecosystem — a pixelated society by D.C.O.T. (2014–2026). Holding **any** of these also unlocks the free Collector Tutor agent.

| Name | Address | Chain | Notes |
|---|---|---|---|
| **Travelers** (original) | `0xdc9430d36a30dfd732c16c63238b31c5a84fd98e` | Base | 71 unique · 2,664 tokens. Mint closed. |
| **LPC Residents** | `0x718eb4067ea4c8f0eae0b7f7beeaeef463b73d4f` | Base | DEGEN MUTATIO, lebleuleFam, ⌐U‑F‑O. |
| **Mutant Lost Pixel City** | `0xb458397525ac01fc4b4a2fca8470121621c21c66` | Base | 4 unique · 137 tokens. Airdrop to top LPC owners. |
| **DANKGEN series** | `0x5458df6631d4c1061f6a3755b74e482bd96f5226` | Base | 365/365 · fully on‑chain pixel edition. |
| **RE‑BURN** | `0xe9043dd09da79c23307613655fce2003191e9b18` | Base | Open edition · burn‑to‑mint (0.01 ETH). |
| **Lost Pixel City V1** | `0xc3e18e0c5e373dbee63a35d0cdf3acb92cb7a0e5` | Ethereum | Burn Travelers to create new LPC characters (0.0069 ETH + burn). |
| **Lost Pixel City DAO** | `0xa11493d5799d8cbaa52b567e45588f617df18d0f` | Ethereum | Bonding‑curve membership; co‑owns one of each Traveler. |

## 5. AI Agents (ERC‑8257 tools)

| Item | Value |
|---|---|
| **Agent Tool Registry** | `0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1` (Ethereum + Base) |
| **Collector Tutor** | `toolId 114` (Ethereum) — free, holder‑gated |
| **Pixel‑Art Generator** | `toolId 115` (Ethereum) — hold‑to‑access $BOTTT |
| **Voxel Architect** | in training (not yet registered) |

Full details in [AGENTS.md](./AGENTS.md).

---

## Minimal ABIs (common interfaces)

### ERC‑721 (collections)
```solidity
function ownerOf(uint256 tokenId) view returns (address);
function balanceOf(address owner) view returns (uint256);
function tokenURI(uint256 tokenId) view returns (string);   // returns on-chain data:image/svg+xml;base64 or JSON
function totalSupply() view returns (uint256);
function transferFrom(address from, address to, uint256 tokenId);
```

### $BOTTT (ERC‑20, EIP‑2612)
```solidity
function balanceOf(address) view returns (uint256);         // used for hold-to-access gating
function name() view returns (string);                      // "LPC-BOT"
function symbol() view returns (string);                    // "BOTTT"
function decimals() view returns (uint8);                   // 18
function DOMAIN_SEPARATOR() view returns (bytes32);         // EIP-2612 permit supported
function permit(address owner,address spender,uint256 value,uint256 deadline,uint8 v,bytes32 r,bytes32 s);
// NOTE: P2P transfer/transferFrom REVERT for normal wallets (Uniswap V4 transfer-gated).
// Acquire by BUYING on the pool; the token is HOLD-to-access, not send-to-pay. See TOKENOMICS.md.
```

### LPLART mint (Pixel‑Art agent target)
```solidity
// Mints on-chain SVG art. Payable 0.0001 ETH + burns 1 PIXEL (one-time PIXEL approve first).
function mint(string svg, string name, string artist, string desc, string portfolio) payable;
```

### ERC‑8257 registry (agents)
```solidity
function registerTool(string metadataURI, bytes32 manifestHash, address accessPredicate) returns (uint256 toolId);
function updateToolMetadata(uint256 toolId, string newURI, bytes32 newHash);
function setAccessPredicate(uint256 toolId, address newPredicate);
function getToolConfig(uint256 toolId) view returns (address creator,string metadataURI,bytes32 manifestHash,address accessPredicate);
event ToolRegistered(uint256 indexed toolId, address indexed creator, address indexed accessPredicate, string metadataURI, bytes32 manifestHash);
event ToolMetadataUpdated(uint256 indexed toolId, string newURI, bytes32 newHash);
```

See [WALLET.md](./WALLET.md) for full signing examples with ethers v6.
