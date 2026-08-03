# Contract state diagrams

Mermaid diagrams of the lifecycle of each contract family. (GitHub renders Mermaid natively.)

## ERC‑721 collection (gems, BOTs, LAND, LPLART, GEM…)

```mermaid
stateDiagram-v2
    [*] --> Unminted
    Unminted --> Owned: mint()
    Owned --> Owned: transferFrom() (new owner)
    Owned --> Burned: transfer to 0xdead / burn()
    Owned --> Owned: (dNFT only) setData()/updateVoxelScene()  %% LPVL parcels
    Burned --> [*]
```

## Lost Pixel Vox LAND (LPVL — dynamic NFT)

```mermaid
stateDiagram-v2
    [*] --> Claimable
    Claimable --> Owned: free GEM-gated claim (#N -> #N)
    Owned --> Edited: setData(scene) / setProgram()
    Edited --> Edited: rewrite-history / updateVoxelScene()
    Owned --> Owned: transferFrom()
    note right of Edited: voxel scene persists 100% on-chain (RLE)
```

## $BOTTT (ERC‑20, transfer‑gated)

```mermaid
stateDiagram-v2
    [*] --> Minted
    Minted --> HeldByWallet: buy on Uniswap V4 pool
    HeldByWallet --> Pool: sell (pool/factory/distributor only)
    HeldByWallet --> Burned: burn()
    HeldByWallet --> HeldByWallet: hold (unlocks agents via balanceOf)
    note right of HeldByWallet: P2P transferFrom REVERTS (InvalidTransfer)\nhold-to-access, not send-to-pay
```

## PIXEL / mint flow (LPLART pixel‑art)

```mermaid
sequenceDiagram
    participant U as User wallet
    participant P as PIXEL (Resources)
    participant L as LPLART
    U->>P: approve burn (one-time)
    U->>L: mint(svg,...) payable 0.0001 ETH
    L->>P: burn 1 PIXEL
    L-->>U: NFT minted (on-chain SVG) -> auto-indexed on the map
```

## ERC‑8257 agent tool

```mermaid
stateDiagram-v2
    [*] --> Unregistered
    Unregistered --> Registered: registerTool(uri, hash, predicate) [creator only]
    Registered --> Registered: updateToolMetadata(id, uri, hash) [creator only]
    Registered --> Indexed: OpenSea crawls registry
    Indexed --> Callable: POST endpoint (gate: holder / hold-to-access)
    Registered --> Deregistered: deregisterTool(id)
    Deregistered --> [*]
```
