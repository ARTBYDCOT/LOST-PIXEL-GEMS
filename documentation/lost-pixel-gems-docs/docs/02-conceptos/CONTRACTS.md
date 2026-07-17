# Smart Contracts

Lost Pixel Gems is built to be **fully on-chain** and **auditable**. Two layers:

1. **Existing collections** (live on Ethereum) — the art NFTs.
2. **Protocol contracts** (open for development & audit) — PIXELS, voxel-LAND mint, on-chain map archive.

## 1. Live collections (Ethereum mainnet)

| # | Name | Address | Notes |
|---|---|---|---|
| 1 | **LPG V1** | `0xb52cD7A93878D823dF0fBc4F2E5a42f7b5B53A44` | The 111 gems; owner-gate for the map |
| 2 | **LPG V2 / LPGNTRCTV** | `0xb8698f54BEAd61D0C34e60Ab49d5AC992674f01B` | Companion collection |
| 3 | **LPL** | `0x80910b1210f2bdcb1122cac6b76a3ed28c9c695c` | — |
| 4 | **LPGR** | `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548` | — |
| 5 | **LPC-BOT / BOTTT** | `0x3560dc18d27888de170acbc119442db3fdcf5ccf` | Avatar/bot tier |
| 6 | **ABS** | `0x848f15ba0a652b09438c9747e80304147d87aa0a` | — |

Read-only calls used by the site (via public RPC, no keys): `balanceOf`, `ownerOf`, `totalSupply`. ABIs in `contracts/abi/`.

## 2. Protocol contracts — **open for development & audit**

These implement the [deflationary economy](ECONOMY.md). They are the **priority for contributors** (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

### `PIXELS` (ERC-20)
- Fixed genesis supply, **no post-genesis emission**, `burn` / `burnFrom`.
- The only sink is the LAND mint.

### `VoxelLAND` (ERC-721)
```solidity
// burns PIXELS proportional to the model's voxel count, mints the model, records position
function mintVoxel(bytes calldata voxelData, uint256 x, uint256 z) external returns (uint256 tokenId);
```
- **Burns PIXELS ∝ voxels** (pricing tiers in [ECONOMY.md](ECONOMY.md#3-burn-to-mint-pricing-per-construction)).
- Stores the `.vox` payload / hash + coordinates so the map is **rebuildable from chain data alone**.
- Position **owner-locked**; unlocked drafts movable by anyone.

### `MapArchive`
- Append-only record of **kept blocks + metadata** → the permanent 8M-voxel micro-universe.
- Emits `VoxelSceneUpdated` for indexers/the map.

### `Exhibition` (view-only)
- A **6-word signed message** enables displaying a wallet's NFTs in a room.
- **No transfer, no approval** — display permission only; NFTs stay in the collector's wallet.

## Audit invitation
All protocol contracts are meant to be **reviewed in the open** before mainnet deployment. Threat models, formal specs, and independent audits are welcome — open an `audit/…` PR or a Security advisory (see [SECURITY.md](../SECURITY.md)).
