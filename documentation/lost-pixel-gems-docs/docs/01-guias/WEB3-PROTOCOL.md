# Lost Pixel City — Fully On-Chain Voxel Map Protocol

**A permanent, unstoppable voxel world where every model, its position and its owner live 100% on Ethereum. No database. The EVM is the visual engine; the website is just one renderer of open, on-chain state.**

- **Network:** Ethereum mainnet
- **License:** MIT (open protocol — anyone can read the world and build their own client)
- **Live map:** https://lostpixelgems.space/

---

## 1. Smart Contracts

| Contract | Address | Standard | Role |
|---|---|---|---|
| **LPG-MAIN-ASSETS** (`LPGMA`) | [`0x0e8d7fe83d4a1bc1fcb812862af28227abb9e138`](https://etherscan.io/address/0x0e8d7fe83d4a1bc1fcb812862af28227abb9e138) | ERC-721 | Fully on-chain voxel NFTs. The model's `.vox` bytes + name + size live on-chain; `tokenURI` renders an on-chain **SVG image** + a self-contained **interactive HTML** animation. |
| **VOXEL MAP · Genesis Map 1** | [`0x513493926EedeE69B6a8d65a1068CFa87855dad3`](https://etherscan.io/address/0x513493926EedeE69B6a8d65a1068CFa87855dad3) | Protocol | The public map, stored 100% on-chain. Each **unique cell** holds an owner + position + rotation + the voxel bytes. The website rebuilds the world by reading this contract. |
| **PIXELS** (LPGR token #2) | [`0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548`](https://etherscan.io/nft/0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548/2) | ERC-1155 | The deflationary **fuel**. Burned to mint assets and to seal/move positions. |

New maps in the future = new VoxelMap deployments (Map 2, Map 3 …). The same asset (LPGMA token) can be placed across any map — a fully on-chain museum of reusable voxel resources.

---

## 2. The PIXELS Burn Protocol

**PIXELS = LPGR token #2**, an ERC-1155. Burning = an irreversible `safeTransferFrom(you → 0x…dEaD, id 2, amount)`. Nothing is ever minted back; supply only goes down.

### Burn Costs

| Action | PIXELS Burned |
|---|---|
| **Mint** a 32³ asset | 1 |
| **Mint** a 64³ asset | 2 |
| **Mint** a 128³ asset | 3 |
| **Mint** a 256³ asset | 6 |
| **Seal a position** on the map (`place`) | 1 (flat) |
| **Move** an existing position (`moveMyPlacement`) | 1 (flat) |

- Minting cost scales with **size** (bigger canvas = more PIXELS).
- Positioning is a **flat 1 PIXEL**, regardless of size — you pay for *permanence of place*, not size.
- Before any burn, you approve once: `LPGR.setApprovalForAll(<contract>, true)` so the contract can move your PIXELS to the burn address.

**Who can use it?** Anyone who owns and burns PIXELS. There is no allow-list for creating — only deploying/config is the deployer's. Burn PIXELS → create in the open world.

---

## 3. Rules of the World (Immutability)

- A model's **name and voxel design are immutable forever** — set once at mint, never editable by anyone (not even the deployer).
- Only a placement's **position** can change, and only by its owner, burning 1 PIXEL per move.
- **Every cell is unique** — no two models can overlap the same position/layer. First to seal it, owns it.
- Big sizes (128³, 256³) cannot stack vertically; small sizes can use layers.

---

## 4. How to Participate in the Open World

```
BUILD ──▶ MINT (burn PIXELS by size) ──▶ PLACE (burn 1 PIXEL) ──▶ VISIT
 editor      LPG-MAIN-ASSETS NFT            VoxelMap cell         public map
```

### Step-by-Step Guide

1. **Build** a voxel model in the editor
   - Hidden interior voxels are auto-culled (hollow) so the on-chain payload stays small and cheap
   - *Keep it small — data is the cost*

2. **Mint** it as an `LPG-MAIN-ASSETS` NFT
   - This burns PIXELS by size and writes the `.vox` bytes + your permanent name on-chain
   - Size class determines the burn cost (1 to 6 PIXELS)

3. **Place** it on Genesis Map 1 at a free, unique cell
   - This burns 1 PIXEL and seals your `owner + x + z + rotation + voxels` into the map contract forever
   - Only you can edit your parcel via your private key

4. **Visit** — walk the public map as a pixel and stand in front of your parcel
   - The map reads the live contract state; what you see *is* the chain
   - Your creation is permanent and accessible forever

### Practical Size Guide

**Note:** Fully on-chain = gas scales with voxel count

| Voxels | Result |
|---|---|
| ≲ 3,000 | cheap ✅ |
| ~10,000 | near the top of what's mintable |
| 40k–86k+ | won't fit in a block — split into smaller pieces |

---

## 5. Smart Contract Functions

### LPG-MAIN-ASSETS (ERC-721)

```solidity
// Create a new voxel NFT asset
function mint(bytes vox, string name_, uint8 sizeClass) payable returns (uint256);

// Query functions
function voxOf(uint256 id) view returns (bytes);        // on-chain voxel bytes
function assetName(uint256 id) view returns (string);   // asset name
function sizeOf(uint256 id) view returns (uint8);       // size class (1-6)
function creatorOf(uint256 id) view returns (address);  // original creator
function tokensOfOwner(address o, uint256 scanTo) view returns (uint256[]);

// Metadata
function tokenURI(uint256 id) view returns (string);    // 100% on-chain: SVG image + interactive HTML
```

### VOXEL MAP (Genesis Map 1)

```solidity
// Place a voxel on the map (burns 1 PIXEL)
function place(
  uint64 x, 
  uint64 z, 
  uint16 layer, 
  uint8 sizeClass, 
  uint8 rot, 
  string name, 
  bytes vox
) payable;

// Move an existing placement (burns 1 PIXEL)
function moveMyPlacement(
  uint256 fromId, 
  uint64 newX, 
  uint64 newZ, 
  uint16 newLayer, 
  uint8 newRot
) payable;

// Query functions
function count() view returns (uint256);                 // total placements
function cellAtIndex(uint256 i) view returns (uint256 cellId);
function placementByCell(uint256 id) view returns (
  address owner,
  uint64 x,
  uint64 z,
  uint32 placedAt,
  uint8 sizeClass,
  uint8 rot,
  uint16 layer,
  string name,
  bytes vox
);
function cellId(uint64 x, uint64 z, uint16 layer) pure returns (uint256);
```

---

## 6. Read the World Yourself

The world is public state — build your own game/renderer over it using the open SDK (MIT):

```javascript
import { LPCMap } from './lpc-map-sdk.js';
import { ethers } from 'ethers';

// Read the entire world from the Ethereum blockchain
const world = await LPCMap.read('0x513493926EedeE69B6a8d65a1068CFa87855dad3', {
  ethers,
  rpc: 'https://ethereum-rpc.publicnode.com',
  max: 400
});
// world = { name, mapNumber, canvas:{w,h}, placements:[ { id, owner, x, z, rot, name, vox } ] }

// Parse and render voxel data
for (const p of world.placements) {
  const voxels = LPCMap.parseVox(p.vox);   // [{ x, y, z, r, g, b }] — z-up
  // …render however you like in your own application
}
```

**Key advantages:**
- No API keys required
- No servers needed
- No permission gates
- The map contract *is* the backend

---

## 7. On-Chain Metadata (Fully Self-Contained)

`LPG-MAIN-ASSETS.tokenURI` returns a base64 JSON where **every media field is a data URI** — zero external fetches:

- **image** → on-chain **SVG** (front projection, run-length encoded) — renders directly on Etherscan
- **animation_url** → self-contained **HTML**: the voxel bytes (base64) + an inline JS renderer + link buttons to the private viewer and public map
- **name**, **description**, **attributes** (incl. `Storage: 100% on-chain`) → on-chain JSON

**Result:** The token renders completely from the contract alone. The links are navigation only and do not affect the on-chain status.

---

## 8. How to Get PIXELS

PIXELS are the deflationary fuel of the Lost Pixel Gems ecosystem. To participate:

1. **Acquire PIXELS**
   - Purchase on secondary markets (DEX, OpenSea, etc.)
   - Participate in community airdrops
   - Receive from ecosystem activities

2. **Approve the VoxelMap contract**
   ```
   LPGR.setApprovalForAll(0x513493926EedeE69B6a8d65a1068CFa87855dad3, true)
   ```

3. **Burn PIXELS to create**
   - Each action (mint asset or place on map) burns PIXELS irreversibly
   - The burn address is `0xdEaD…` (dead wallet)
   - Supply only decreases — creating makes PIXELS more scarce

---

## 9. Community & Support

- **Protocol is open source** — MIT license
- **Anyone can deploy a map** — the VoxelMap contract pattern is public
- **Cross-map compatibility** — the same assets work across Genesis Map 1, Map 2, and future maps
- **Open to audits and contributions** — see CONTRIBUTING.md and SECURITY.md

---

## 10. Key Principles

✅ **100% On-Chain** — No external databases, no cloud storage, no IPFS. Everything lives on Ethereum forever.

✅ **Immutable Art** — Once created and placed, your voxel art cannot be deleted or edited by anyone but you.

✅ **Deflationary Economy** — Every creation burns PIXELS. Supply only decreases. Value accrues to permanence.

✅ **Open Protocol** — Anyone can read the world, deploy a new map, or build a new renderer. No permission needed.

✅ **Sovereign Creator** — You own your creations via your wallet. Your private key is your only gate.

---

**Lost Pixel City — art by D.C.O.T. Burn PIXELS. Create forever.**

*The world lives on Ethereum. What you build today will exist in 100 years.*
