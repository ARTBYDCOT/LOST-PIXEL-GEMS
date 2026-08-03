# The on‑chain map is open source

The Lost Pixel voxel world is **100% on‑chain** — the placement data lives in the **Voxel Map** contracts. Because it's on‑chain and **CC0**, anyone can **read a region and embed it** in their own website to build a game or experience. You don't ask permission; you point at coordinates and render.

| Map | Contract | Chain |
|---|---|---|
| Genesis Map 1 | `0x5134f5df64c2b62a70Bcb5A96e1B8Cbf6C6B7dad3` | Ethereum |
| Map 2 (Base) | `0xe2bf4C47DE9876b8e55e352A05362caA2e1437A7` | Base |

## The coordinate triad `(x, y, z)`

Every voxel and every parcel is addressed by a **triad**:

```
        y (up / height)
        │
        │
        └────── x (east ↔ west, along the map length)
       ╱
      ╱
     z (north ↔ south, depth)
```

| Axis | Meaning | Typical range |
|---|---|---|
| **x** | position along the map length (E–W) | `0 … 7999` (public map is ~8000 wide) |
| **y** | height (up) | `0 … 255` |
| **z** | depth (N–S) | `0 … 255` |

A **region** you want to capture = an **origin** `(x, y, z)` + a **size** `(w, h, d)`:

```
region = { x: 1200, y: 0, z: 40, w: 64, h: 48, d: 64 }
// captures a 64×48×64 block starting at (1200, 0, 40)
```

## Embed it in your site (iframe)

Drop the embeddable viewer into any page and pass the region in the URL:

```html
<iframe
  src="https://lpc-bot.art/map-embed.html?x=1200&y=0&z=40&w=64&h=48&d=64&map=0x5134f5df64c2b62a70Bcb5A96e1B8Cbf6C6B7dad3&chain=1"
  width="800" height="480" style="border:0;border-radius:12px"
  allow="fullscreen"></iframe>
```

The viewer renders the coordinate triad, the captured region box, and the on‑chain voxels of that region. It's a ready starting point for a game/experience over that slice of the world.

### Talk to the embed (postMessage)

```js
const frame = document.querySelector('iframe');
// receive the region + a click's voxel coordinate
window.addEventListener('message', (e) => {
  if (e.data?.type === 'lpc-map:click') console.log('voxel', e.data.voxel); // {x,y,z,hex}
  if (e.data?.type === 'lpc-map:ready') console.log('region', e.data.region);
});
// move the captured region at runtime
frame.contentWindow.postMessage({ type:'lpc-map:setRegion', region:{ x:2000, y:0, z:0, w:96, h:64, d:96 } }, '*');
```

## Read a region directly on‑chain (no iframe)

If you'd rather render it yourself, read the region's voxels from the map contract and draw them (e.g. Three.js instanced cubes). Feed the result to the viewer via `?voxels=<url-returning-json>` or your own renderer.

```ts
// viem — pseudo-read of a region (adapt to the contract's read function)
const scene = await client.readContract({
  address: '0x5134f5df64c2b62a70Bcb5A96e1B8Cbf6C6B7dad3',
  abi: parseAbi(['function regionData(uint256 x,uint256 y,uint256 z,uint256 w,uint256 h,uint256 d) view returns (bytes)']),
  functionName: 'regionData', args: [1200n,0n,40n,64n,48n,64n],
});
// scene is RLE-encoded voxels → decode → [{x,y,z,hex}, …]
```

> The exact read function name may differ per map version — check the verified contract on the explorer. The **data is public and on‑chain**, so any decoder works; the format is CC0.

## Why this matters

- **Composable world:** anyone can build a mini‑game, a gallery, or an experience anchored to a real on‑chain location.
- **Permissionless & CC0:** no API keys, no gatekeepers — the map is the common.
- **Persistent:** what a LAND owner builds (via `setData`/`updateVoxelScene`) is what your embed shows, live from chain.

See **`map-embed.html`** (bundled in the site) for the reference embeddable viewer.
