# LPG-MAIN-ASSETS Contract — Updated Deployment

## 🎨 Voxel NFT Contract on Ethereum Mainnet

---

## Contract Information

| Property | Value |
|---|---|
| **Contract Name** | LPG-MAIN-ASSETS |
| **Symbol** | LPGMA |
| **Standard** | ERC-721 (NFT) |
| **Network** | Ethereum Mainnet |
| **Address** | [`0xa0795E3665552A1ea784e8e0d465A6E65455b51B`](https://etherscan.io/address/0xa0795E3665552A1ea784e8e0d465A6E65455b51B) |
| **Status** | ✅ Active & Live |

---

## What is LPG-MAIN-ASSETS?

**LPG-MAIN-ASSETS (LPGMA)** is the core ERC-721 NFT contract for Lost Pixel Gems. It stores fully on-chain voxel models where:

- ✅ **Voxel data** (`.vox` bytes) lives 100% on Ethereum
- ✅ **Model names** are immutable forever
- ✅ **Size classification** determines minting cost in PIXELS
- ✅ **Metadata** renders as on-chain SVG + interactive HTML
- ✅ **No external dependencies** — complete self-contained NFTs

---

## How It Works

### Minting a Voxel NFT

```solidity
function mint(bytes vox, string name_, uint8 sizeClass) payable returns (uint256);
```

**To create a voxel NFT:**

1. Build your model in the editor
2. Export as `.vox` format
3. Burn PIXELS according to size:
   - 32³ = 1 PIXEL
   - 64³ = 2 PIXELS
   - 128³ = 3 PIXELS
   - 256³ = 6 PIXELS

4. Call `mint()` with:
   - `vox` — the voxel data bytes
   - `name_` — your creation's permanent name
   - `sizeClass` — dimension class (1-6)

5. **Result:** You receive an LPGMA NFT token in your wallet

---

## Key Functions

### Querying

```solidity
// Get the voxel data of any NFT
function voxOf(uint256 id) view returns (bytes);

// Get the creator's name for the asset
function assetName(uint256 id) view returns (string);

// Get the size class (determines pixel dimensions)
function sizeOf(uint256 id) view returns (uint8);

// Get the original creator's address
function creatorOf(uint256 id) view returns (address);

// List all tokens owned by an address
function tokensOfOwner(address o, uint256 scanTo) view returns (uint256[]);

// Get full metadata (SVG image + interactive HTML)
function tokenURI(uint256 id) view returns (string);
```

### Properties

**Immutable Design:**
- Model name — set at creation, never changes
- Voxel data — stored permanently on-chain
- Creator — permanently recorded
- Size class — fixed at mint

---

## On-Chain Metadata

Each LPGMA token's `tokenURI()` returns a base64-encoded JSON containing:

### Image
- **SVG rendering** of the voxel model (front projection)
- **Run-length encoded** for compact storage
- Renders directly on Etherscan

### Animation
- **Self-contained HTML** with:
  - Voxel data embedded (base64)
  - Interactive 3D viewer (JavaScript)
  - Navigation links to map/gallery
  - Full functionality without external APIs

### Metadata
- Token name
- Description
- Attributes (including "Storage: 100% on-chain")
- Creator information

**Result:** Complete NFT rendered from contract alone. Zero external dependencies.

---

## Using Your LPGMA NFT

### Display in a Room
Once you own an LPGMA token, you can:
1. Load it into a private **Voxel Room**
2. Place it on the **Public Voxel Map** (costs 1 PIXEL)
3. Share it with the community

### Place on the Public Map

To add your LPGMA to the Lost Pixel City map:

```solidity
// VOXEL MAP contract
function place(
  uint64 x, 
  uint64 z, 
  uint16 layer, 
  uint8 sizeClass, 
  uint8 rot, 
  string name, 
  bytes vox
) payable;
```

**Cost:** 1 PIXEL (flat rate, regardless of size)

**Result:** Your voxel model is sealed to a unique (x, z) coordinate on the map forever.

---

## Size Reference

### Dimension Classes

| Class | Dimensions | PIXELS to Mint | Stacking | Best For |
|---|---|---|---|---|
| 1 | 32³ | 1 | Stackable | Small decorations |
| 2 | 64³ | 2 | Stackable | Medium objects |
| 3 | 128³ | 3 | Single layer | Large structures |
| 4 | 256³ | 6 | Single layer | Massive builds |

### Voxel Count Guide

| Voxel Count | Gas Cost | Recommendation |
|---|---|---|
| < 3,000 | Low 💚 | Ideal |
| 3,000–10,000 | Medium 🟡 | Good |
| 10,000–40,000 | High 🔴 | Consider splitting |
| > 40,000 | Very High 🔥 | Split into multiple |

---

## Security & Immutability

✅ **Once minted, your LPGMA NFT cannot be:**
- Modified or edited
- Deleted or burned by anyone but you
- Changed in name or appearance

✅ **Only you can:**
- Move it on the map (if placed)
- Sell it on marketplaces
- Transfer it to another wallet

✅ **The contract cannot:**
- Modify your voxel data
- Change your model's name
- Add backdoor functions
- Allow unauthorized transfers

---

## Exploring LPGMA Tokens

### On Etherscan
View any LPGMA token directly:
```
https://etherscan.io/token/0xa0795E3665552A1ea784e8e0d465A6E65455b51B?a=[owner_address]
```

### On OpenSea
Coming soon — full marketplace integration for trading LPGMA tokens.

### On the Map
Visit the Lost Pixel City public map to see placed LPGMA NFTs:
```
https://lostpixelgems.space/
```

---

## Contract Interactions

### To Mint (Web3.js example)

```javascript
import { ethers } from 'ethers';

const LPGMA_ADDRESS = '0xa0795E3665552A1ea784e8e0d465A6E65455b51B';
const LPGMA_ABI = [...]; // Full ABI from Etherscan

const contract = new ethers.Contract(LPGMA_ADDRESS, LPGMA_ABI, signer);

// Mint a new voxel NFT
const tx = await contract.mint(
  voxelDataBytes,    // bytes
  "My Voxel Model",  // string name
  2                  // uint8 sizeClass (64³)
);

const receipt = await tx.wait();
console.log('Minted token ID:', receipt.events[0].args.tokenId);
```

### To View Token Data

```javascript
const tokenId = 1;
const voxels = await contract.voxOf(tokenId);
const name = await contract.assetName(tokenId);
const size = await contract.sizeOf(tokenId);
const creator = await contract.creatorOf(tokenId);
const metadata = await contract.tokenURI(tokenId);

console.log({
  voxels,      // bytes
  name,        // "My Voxel Model"
  size,        // 2 (64³)
  creator,     // 0x...
  metadata     // base64 JSON
});
```

---

## Statistics

- **Standard:** ERC-721
- **Storage:** 100% on-chain
- **Supply:** Open (limited by PIXELS available)
- **Transferable:** Yes (standard NFT transfers)
- **Burnable:** Only by owner
- **Upgradeable:** No (immutable by design)

---

## Links

🔗 **Contract:** https://etherscan.io/address/0xa0795E3665552A1ea784e8e0d465A6E65455b51B

🔗 **Tokens:** https://etherscan.io/token/0xa0795E3665552A1ea784e8e0d465A6E65455b51B

🔗 **Live Map:** https://lostpixelgems.space/

📖 **Full Protocol:** [WEB3-PROTOCOL.md](WEB3-PROTOCOL.md)

---

## Support & Audits

This contract is:
- ✅ Open-source (MIT License)
- ✅ Ready for external audits
- ✅ Community-reviewed
- ✅ Secure by design (immutable)

Questions or security concerns? See [SECURITY.md](SECURITY.md) or open an audit PR on [GitHub](https://github.com/ARTBYDCOT/LOST-PIXEL-GEMS).

---

**LPG-MAIN-ASSETS — Your voxel art lives forever on Ethereum.**

*Burn PIXELS. Create freely. Own permanently.*
