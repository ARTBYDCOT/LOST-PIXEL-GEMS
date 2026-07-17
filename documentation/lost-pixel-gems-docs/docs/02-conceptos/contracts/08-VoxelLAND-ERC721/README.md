# VoxelLAND Contract (ERC-721)

## Overview
VoxelLAND is the core protocol contract for building the Lost Pixel Gems map on-chain. It implements a burn-to-mint mechanism where PIXELS are burned proportional to voxel count to mint unique voxel terrain NFTs.

## Contract Details
- **Type:** ERC-721 NFT Collection
- **Network:** Ethereum Mainnet
- **Purpose:** On-chain voxel terrain construction and ownership
- **Status:** Open for development & audit

## Core Mechanism

### Burn-to-Mint Function
```solidity
function mintVoxel(bytes calldata voxelData, uint256 x, uint256 z) external returns (uint256 tokenId);
```

**Functionality:**
- Burns PIXELS proportional to the model's voxel count
- Mints a unique VoxelLAND NFT (ERC-721)
- Records position coordinates (x, z)
- Stores complete voxel data on-chain

## Features

### Data Storage
- Stores `.vox` payload and hash
- Records x, z coordinates
- Map rebuildable from chain data alone
- Immutable on-chain record

### Position Management
- **Owner-locked positions:** Placed constructions locked to owner
- **Unlocked drafts:** Can be moved by anyone before finalization
- Enables collaborative building and positioning

### Pricing Model
- Burn amount based on voxel count
- Pricing tiers defined in [ECONOMY.md](../../ECONOMY.md#3-burn-to-mint-pricing-per-construction)
- Deflationary economy mechanism

## Technical Specifications
- Standard ERC-721 functionality
- Read-only calls: `balanceOf`, `ownerOf`, `totalSupply`
- Custom function: `mintVoxel(bytes, uint256, uint256)`
- ABI available in `contracts/abi/`

## Resources
- **Art & Models:** See `/art` folder for voxel terrain artwork and models
- **Documentation:** See `/docs` folder for detailed specifications
- **Smart Contract Code:** See `contracts/` folder in main repo
- **RPC:** Public RPC endpoint (no keys required)

## Use Cases
- Construct and own terrain NFTs
- Participate in map building
- Create unique voxel environments
- Burn PIXELS for ecosystem participation

## Audit Status
Protocol contract open for development and community audit. Security reviews welcome.

---
**Last Updated:** 2026
**Status:** ✅ Open for Audit & Development
