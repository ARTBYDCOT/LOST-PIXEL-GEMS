# Wallet — connection & signing

All signing happens **in the user's own wallet** (MetaMask / any EIP‑1193 provider). The apps never hold private keys. Examples use **ethers v6** (UMD or ESM).

```html
<script src="https://cdn.jsdelivr.net/npm/ethers@6.13.4/dist/ethers.umd.min.js"></script>
```

## 1. Connect + get a signer

```js
if (!window.ethereum) throw new Error('Install MetaMask or an EIP-1193 wallet');
const provider = new ethers.BrowserProvider(window.ethereum);
const signer   = await provider.getSigner();
const address  = await signer.getAddress();
```

## 2. Switch chain (Ethereum L1 / Base)

```js
// Ethereum mainnet
await window.ethereum.request({ method:'wallet_switchEthereumChain', params:[{ chainId:'0x1' }] });
// Base (8453)
await window.ethereum.request({ method:'wallet_switchEthereumChain', params:[{ chainId:'0x2105' }] });
```

## 3. Read‑only ownership / holdings (holder gates)

The Collector Tutor is free but **holder‑gated**; paid agents are **hold‑to‑access**. Both are `balanceOf` reads (no signature, no gas):

```js
const ERC20_ABI = ['function balanceOf(address) view returns (uint256)'];
const bottt = new ethers.Contract('0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75', ERC20_ABI, provider);
const bal   = await bottt.balanceOf(address);              // 18 decimals
const holds100k = bal >= (100000n * 10n ** 18n);           // Pixel-Art gate

// NFT holder gate — hold ANY ecosystem ERC-721
const ERC721_ABI = ['function balanceOf(address) view returns (uint256)'];
const lpg = new ethers.Contract('0xb52cD7A93878D823dF0fBc4F2E5a42f7b5B53A44', ERC721_ABI, provider);
const ownsLPG = (await lpg.balanceOf(address)) > 0n;
```

> The gateway does this server‑side across all ecosystem + Travelers collections (multi‑chain, cached) via `GET /api/owns?address=0x…` → `{ owner, hits }`.

## 4. Mint pixel‑art on‑chain (LPLART) — approve PIXEL + mint

The Pixel‑Art flow is **self‑mint**: the editor builds an on‑chain SVG and calls `mint` (payable `0.0001 ETH`, burns `1 PIXEL`). One‑time PIXEL approval first.

```js
const PIXEL = '0x6912dfdb9cff40a20fd1c297374bcbbd5d6dc548'; // Resources (PIXEL token #2)
const LPLART = '0x84198807972F196ED7D8b18B3B7A55B14237C0ea';

// (1) one-time approve the PIXEL burn (ERC-1155/2612 style, per the Resources contract)
//     — the Lost Pixel Studio handles the exact approve call; conceptually:
await window.ethereum.request({ method:'eth_sendTransaction', params:[{ from:address, to:PIXEL, data: approveData }] });

// (2) mint
const iface = new ethers.Interface(['function mint(string,string,string,string,string) payable']);
const data  = iface.encodeFunctionData('mint', [svg, name, artist, desc, portfolio]);
const hash  = await window.ethereum.request({ method:'eth_sendTransaction', params:[{
  from: address, to: LPLART, data, value: '0x5AF3107A4000' /* 0.0001 ETH */
}]});
```

## 5. Register / update an ERC‑8257 tool (agents)

Only the **creator wallet** can register/update its tools (the registry enforces `NotToolCreator`).

```js
const REGISTRY = '0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1';
const ABI = [
  'function registerTool(string metadataURI, bytes32 manifestHash, address accessPredicate) returns (uint256)',
  'function updateToolMetadata(uint256 toolId, string newURI, bytes32 newHash)',
  'event ToolRegistered(uint256 indexed toolId, address indexed creator, address indexed accessPredicate, string metadataURI, bytes32 manifestHash)'
];
const registry = new ethers.Contract(REGISTRY, ABI, signer);

// manifestHash = keccak256 of the JCS-canonicalized manifest bytes
function canon(o){                                   // deterministic sorted-key canonicalization
  if (Array.isArray(o)) return '['+o.map(canon).join(',')+']';
  if (o && typeof o==='object') return '{'+Object.keys(o).sort().map(k=>JSON.stringify(k)+':'+canon(o[k])).join(',')+'}';
  return JSON.stringify(o);
}
const manifest = await fetch(metadataURI).then(r=>r.json());
const manifestHash = ethers.keccak256(ethers.toUtf8Bytes(canon(manifest)));

// register (accessPredicate 0x0 = open on registry; gate enforced by the agent server)
const tx = await registry.registerTool(metadataURI, manifestHash, ethers.ZeroAddress);
const rc = await tx.wait();
// toolId from the ToolRegistered event (topics[1])

// update metadata (e.g. new image / access model)
await registry.updateToolMetadata(114, metadataURI, newHash);
```

> A ready‑made browser console is included: **`deploy-tools.html`** — connect wallet → Register / Update the tools with one click.

## 6. EIP‑2612 permit ($BOTTT)

`$BOTTT` supports EIP‑2612 `permit` (gasless approval by signature). **However its `transfer`/`transferFrom` revert for normal wallets** (Uniswap V4 transfer‑gated), so it is used as **hold‑to‑access**, not a payment you send. Acquire it by buying on the pool. See [TOKENOMICS](./TOKENOMICS.md).

## Security notes

- No secrets in client code; the gateway's tokens are server‑side only.
- Verify contract addresses against [CONTRACTS.md](./CONTRACTS.md) before signing.
- The agent endpoints are gated server‑side (`402` when the holder/hold requirement isn't met).
