# PIXELS Contract (ERC-20)

## Overview
PIXELS is the native token of the Lost Pixel Gems ecosystem, implementing a deflationary economy model. It is the only sink for PIXELS in the system through the LAND minting process.

## Contract Details
- **Type:** ERC-20 Token
- **Network:** Ethereum Mainnet
- **Supply Model:** Fixed genesis supply
- **Emission:** No post-genesis emission
- **Status:** Open for development & audit

## Features

### Core Functionality
- Fixed genesis supply (no post-genesis emission)
- Burn functionality: `burn` / `burnFrom`
- The only sink is the LAND mint
- Deflationary economy model

### Technical Specifications
- Standard ERC-20 functions
- Read-only calls: `balanceOf`, `allowance`, `totalSupply`
- ABI available in `contracts/abi/`

## Economic Purpose
- Primary currency for ecosystem participation
- Burned proportionally to voxel count in LAND minting
- Deflationary mechanism ensuring scarcity
- Core to the in-game economy (see [ECONOMY.md](../../ECONOMY.md))

## Burn-to-Mint Mechanism
- Holders burn PIXELS proportional to the model's voxel count
- This enables VoxelLAND (ERC-721) minting
- Pricing tiers defined in [ECONOMY.md](../../ECONOMY.md#3-burn-to-mint-pricing-per-construction)

## Holder Use Cases
- Ecosystem participation
- VoxelLAND (map construction) access
- Economic participation in the ecosystem

## Resources
- **Documentation:** See `/docs` folder for detailed specifications
- **Smart Contract Code:** See `contracts/` folder in main repo
- **RPC:** Public RPC endpoint (no keys required)

## Audit Status
Protocol contract open for development and community audit. Threat models and formal specs welcome.

---
**Last Updated:** 2026
**Status:** ✅ Open for Audit & Development
