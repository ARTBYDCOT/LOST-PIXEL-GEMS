# Lost Pixel Gems - Smart Contracts Directory

Complete reference for all Lost Pixel Gems smart contracts on Ethereum mainnet.

---

## Live Collections (On Ethereum Mainnet)

### 1. LPG V1 - The 111 Gems
- **Address:** `0xb52cD7A93878D823dF0fBc4F2E5a42f7b5B53A44`
- **Type:** ERC-721
- **Supply:** 111 gems
- **Purpose:** Genesis collection; owner-gate for the map
- **Status:** ✅ Live & Active
- **[View Details →](01-LPG-V1/README.md)**

### 2. LPG V2 / LPGNTRCTV - Companion Collection
- **Address:** `0xb8698f54BEAd61D0C34e60Ab49d5AC992674f01B`
- **Type:** ERC-721
- **Purpose:** Companion collection; extended ecosystem participation
- **Status:** ✅ Live & Active
- **[View Details →](02-LPG-V2-LPGNTRCTV/README.md)**

### 3. LPL - Community Collection
- **Address:** `0x80910b1210f2bdcb1122cac6b76a3ed28c9c695c`
- **Type:** ERC-721
- **Purpose:** Core ecosystem participation token
- **Status:** ✅ Live & Active
- **[View Details →](03-LPL/README.md)**

### 4. LPGR - Infrastructure Collection
- **Address:** `0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548`
- **Type:** ERC-721
- **Purpose:** Ecosystem component; supporting infrastructure
- **Status:** ✅ Live & Active
- **[View Details →](04-LPGR/README.md)**

### 5. LPC-BOT / BOTTT - Avatar & Bot Tier
- **Address:** `0x3560dc18d27888de170acbc119442db3fdcf5ccf`
- **Type:** ERC-721
- **Purpose:** Avatar/bot tier; interactive features
- **Category:** Avatar & Bot
- **Status:** ✅ Live & Active
- **[View Details →](05-LPC-BOT-BOTTT/README.md)**

### 6. ABS - Ecosystem Component
- **Address:** `0x848f15ba0a652b09438c9747e80304147d87aa0a`
- **Type:** ERC-721
- **Purpose:** Essential ecosystem component
- **Status:** ✅ Live & Active
- **[View Details →](06-ABS/README.md)**

---

## Protocol Contracts (Open for Development & Audit)

### 7. PIXELS (ERC-20) - Native Token
- **Type:** ERC-20 Token
- **Supply Model:** Fixed genesis, no post-genesis emission
- **Purpose:** Primary currency; burned to mint VoxelLAND
- **Status:** ✅ Open for Audit & Development
- **[View Details →](07-PIXELS-ERC20/README.md)**

### 8. VoxelLAND (ERC-721) - Map Construction
- **Type:** ERC-721 NFT Collection
- **Purpose:** On-chain terrain construction; burn-to-mint mechanism
- **Features:** Voxel data storage, coordinate tracking, position management
- **Status:** ✅ Open for Audit & Development
- **[View Details →](08-VoxelLAND-ERC721/README.md)**

### 9. MapArchive - On-Chain History
- **Type:** Archive Contract
- **Purpose:** Permanent record of kept blocks; 8M-voxel micro-universe
- **Features:** Append-only, event emissions, map reconstruction
- **Status:** ✅ Open for Audit & Development
- **[View Details →](09-MapArchive/README.md)**

### 10. Exhibition - NFT Display
- **Type:** View-Only Contract
- **Purpose:** Permission-based NFT display without transfers
- **Features:** Signed message authorization, read-only access
- **Status:** ✅ Open for Audit & Development
- **[View Details →](10-Exhibition/README.md)**

---

## Quick Reference

### By Purpose
- **Governance & Access:** LPG V1, LPC-BOT
- **Community:** LPG V2, LPL, LPGR, ABS
- **Economy:** PIXELS, VoxelLAND
- **Infrastructure:** MapArchive, Exhibition

### By Type
- **ERC-721 Collections:** LPG V1, V2, LPL, LPGR, LPC-BOT, ABS, VoxelLAND
- **ERC-20 Token:** PIXELS
- **Archive:** MapArchive
- **View-Only:** Exhibition

### By Status
- **Live:** LPG V1, LPG V2, LPL, LPGR, LPC-BOT, ABS
- **Open for Audit:** PIXELS, VoxelLAND, MapArchive, Exhibition

---

## Resource Structure

Each contract folder contains:
- **README.md** - Complete contract overview and specifications
- **/art** - Artwork, designs, and visual assets (public backup)
- **/docs** - Technical documentation and specifications

---

## Integration

### For Developers
- **RPC Endpoint:** Public Ethereum RPC (no authentication required)
- **ABIs:** All contract ABIs available in `contracts/abi/`
- **Read-Only Calls:** `balanceOf`, `ownerOf`, `totalSupply` for collections

### For Auditors
- All protocol contracts welcome external review
- File audit findings: Open `audit/…` PR or Security Advisory
- See [SECURITY.md](../SECURITY.md) for audit procedures

---

## Additional References
- [CONTRACTS.md](../CONTRACTS.md) - Original contract specifications
- [ECONOMY.md](../ECONOMY.md) - Economic model and burn-to-mint pricing
- [TECHNICAL.md](../TECHNICAL.md) - Technical specifications
- [SECURITY.md](../SECURITY.md) - Security and audit procedures

---

**Last Updated:** 2026  
**Network:** Ethereum Mainnet  
**Status:** All contracts live & auditable
