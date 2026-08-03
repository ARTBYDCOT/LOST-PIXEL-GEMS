# Code examples — ethers, viem, Python

The same operations in three stacks. Addresses from [CONTRACTS.md](./CONTRACTS.md).

## Read a holder gate (balanceOf)

### ethers v6 (browser/node)
```js
import { ethers } from 'ethers';
const provider = new ethers.JsonRpcProvider('https://ethereum-rpc.publicnode.com');
const c = new ethers.Contract('0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75',
  ['function balanceOf(address) view returns (uint256)'], provider);
const bal = await c.balanceOf('0xYourWallet');
const unlocksPixel = bal >= 100000n * 10n ** 18n;
```

### viem
```ts
import { createPublicClient, http, parseAbi } from 'viem';
import { mainnet } from 'viem/chains';
const client = createPublicClient({ chain: mainnet, transport: http() });
const bal = await client.readContract({
  address: '0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75',
  abi: parseAbi(['function balanceOf(address) view returns (uint256)']),
  functionName: 'balanceOf', args: ['0xYourWallet'],
});
const unlocksPixel = bal >= 100000n * 10n ** 18n;
```

### Python (web3.py)
```python
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('https://ethereum-rpc.publicnode.com'))
abi = [{"name":"balanceOf","type":"function","stateMutability":"view",
        "inputs":[{"type":"address"}],"outputs":[{"type":"uint256"}]}]
c = w3.eth.contract(address=Web3.to_checksum_address('0xf95f39bef92a8f6b9b8d430d6c1aaaf2a9913d75'), abi=abi)
bal = c.functions.balanceOf('0xYourWallet').call()
unlocks_pixel = bal >= 100_000 * 10**18
```

## Read on‑chain art (tokenURI → SVG)

### viem
```ts
const uri = await client.readContract({
  address: '0x3560dc18d27888de170acbc119442db3fdcf5ccf',   // LPC-BOT
  abi: parseAbi(['function tokenURI(uint256) view returns (string)']),
  functionName: 'tokenURI', args: [100n],
});
// uri is a data:application/json;base64 blob → decode → .image is a data:image/svg+xml;base64
```

### Python
```python
c = w3.eth.contract(address=Web3.to_checksum_address('0x3560dc18d27888de170acbc119442db3fdcf5ccf'),
  abi=[{"name":"tokenURI","type":"function","stateMutability":"view",
        "inputs":[{"type":"uint256"}],"outputs":[{"type":"string"}]}])
print(c.functions.tokenURI(100).call())
```

## Register / update an ERC‑8257 tool (write)

### ethers v6
```js
const registry = new ethers.Contract('0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1',
  ['function registerTool(string,bytes32,address) returns (uint256)',
   'function updateToolMetadata(uint256,string,bytes32)'], signer);
await registry.registerTool(metadataURI, manifestHash, ethers.ZeroAddress);
await registry.updateToolMetadata(114, metadataURI, newHash);
```

### viem (walletClient)
```ts
import { keccak256, toBytes } from 'viem';
const hash = keccak256(toBytes(canonicalManifestString));
await walletClient.writeContract({
  address: '0x265BB2DBFC0A8165C9A1941Eb1372F349baD2cf1',
  abi: parseAbi(['function updateToolMetadata(uint256,string,bytes32)']),
  functionName: 'updateToolMetadata', args: [114n, metadataURI, hash],
});
```

## Call an agent tool (HTTP)

### curl
```bash
curl -X POST "https://…/lpc-agent/api/tools/collector-tutor" \
  -H 'content-type: application/json' \
  -d '{"message":"rarest traits","wallet":"0xYourWallet"}'
```

### Python
```python
import requests
r = requests.post("https://…/lpc-agent/api/tools/pixel-art-mint",
  json={"prompt":"cyberpunk gem","wallet":"0xYourWallet"})
print(r.json())   # {access, studio, art, reply}  (or 402 if not a holder)
```
