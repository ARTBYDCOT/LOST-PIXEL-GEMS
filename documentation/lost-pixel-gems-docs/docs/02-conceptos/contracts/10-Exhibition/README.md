# Exhibition Contract

## Overview
Exhibition is a view-only smart contract that enables NFT display permissions without requiring asset transfers or approvals. Collectors maintain full control of their NFTs while granting display permission for rooms within the Lost Pixel Gems ecosystem.

## Contract Details
- **Type:** View-Only Contract
- **Network:** Ethereum Mainnet
- **Purpose:** Display permissions for NFT exhibition
- **Mechanism:** Signed message authorization
- **Status:** Open for development & audit

## Core Features

### Permission Model
- **No transfer required:** NFTs stay in collector's wallet
- **No approval required:** Only display permission granted
- **Signed message:** 6-word signed message enables display
- **Read-only display:** No asset movement or modification

### Signature-Based Authorization
```
6-word signed message → Display permission → Room exhibition
```

**How it works:**
1. Collector signs a 6-word message
2. Message grants display permission
3. Room can display collector's NFTs
4. Collector retains full ownership and control

### Benefits
- **Security:** No approval vulnerabilities
- **Control:** Collectors control their display permissions
- **Simplicity:** Easy to grant/revoke permissions
- **Privacy:** Granular display control

## Technical Specifications
- View-only smart contract
- Signature verification
- Message-based authorization
- ABI available in `contracts/abi/`

## Integration

### For Collectors
- Display NFT collections in rooms
- Maintain full ownership
- Revoke permissions anytime
- No approval risk

### For Rooms
- Query display permissions via signature verification
- Show collector's NFTs safely
- Verify permission validity
- Cache-friendly queries

## Use Cases
- Personal gallery exhibition
- Collection showcasing
- Community art displays
- Museum-like installations
- Public/private display control

## Resources
- **Documentation:** See `/docs` folder for signature specifications
- **Art & Display Examples:** See `/art` folder for exhibition layouts
- **Smart Contract Code:** See `contracts/` folder in main repo
- **RPC:** Public RPC endpoint (no keys required)

## Audit Status
Protocol contract open for development and community audit. Security reviews welcome.

---
**Last Updated:** 2026
**Status:** ✅ Open for Audit & Development
