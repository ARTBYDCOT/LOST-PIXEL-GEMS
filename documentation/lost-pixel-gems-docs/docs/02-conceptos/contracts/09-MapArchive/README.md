# MapArchive Contract

## Overview
MapArchive is an append-only contract that maintains a permanent record of all kept blocks and metadata within the Lost Pixel Gems ecosystem. It serves as the immutable archive of the growing 8M-voxel micro-universe.

## Contract Details
- **Type:** Archive Contract
- **Network:** Ethereum Mainnet
- **Purpose:** Permanent on-chain record of map state
- **Status:** Open for development & audit

## Core Features

### Append-Only Record
- Records kept blocks and associated metadata
- Immutable historical archive
- No data deletion or modification
- Complete map history on-chain

### Map Archiving
- Preserves the 8M-voxel micro-universe
- Block-by-block permanent record
- Enables complete map history queries
- Disaster recovery and verification

### Event Emissions
```solidity
event VoxelSceneUpdated(/* ... */);
```
- Emits `VoxelSceneUpdated` for indexers and map applications
- Enables real-time map updates for off-chain services
- Supports dApps and visualization tools

## Technical Specifications
- Append-only smart contract
- Emits events for indexing
- Read-only archival functions
- ABI available in `contracts/abi/`

## Integration

### Off-Chain Services
- Event indexers track `VoxelSceneUpdated` emissions
- dApps subscribe to map updates
- Real-time map visualization enabled
- Historical data queries supported

### Map Reconstruction
- Complete map rebuildable from chain data alone
- Permanent disaster recovery mechanism
- Decentralized map backup

## Resources
- **Documentation:** See `/docs` folder for detailed specifications
- **Smart Contract Code:** See `contracts/` folder in main repo
- **Event Schema:** See `/docs` for MapArchive event specifications
- **RPC:** Public RPC endpoint (no keys required)

## Use Cases
- Permanent map history preservation
- On-chain map reconstruction
- Indexer integration
- dApp development
- Data verification and audit

## Audit Status
Protocol contract open for development and community audit. Security reviews welcome.

---
**Last Updated:** 2026
**Status:** ✅ Open for Audit & Development
