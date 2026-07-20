# Voxel Editor — master manual

A complete, tool-by-tool guide to the **Lost Pixel Gems Voxel Editor** (`voxel-studio.html`): design a voxel model, optimize it, render it, and mint it fully on-chain. Every tool, button and shortcut is documented below, straight from the editor itself.

> Live editor: https://lostpixelgems.space/voxel-studio.html

![Voxel Editor overview](docs/img/01-editor-overview.png)

*The layout: **top bar** (undo/redo, resize, render, play) · **left panel** (interaction, brushes, surface, layers, selection) · **3D viewport** (drag to orbit, scroll to zoom) · **right panel** (Go-to links, palette, colour editing, merge, voxelizer, export, mint).*

---

## 0. Quick start

1. **Start on the smallest canvas (32³).** More colours & detail raise the on-chain mint price — build cheaply first.
2. Pick a colour in the **Palette**, choose **Add** + a **brush** (Single is easiest), and click in the viewport to place voxels.
3. **Orbit** by dragging, **zoom** with the wheel. Right-drag / two-finger to rotate on mobile.
4. When happy: **⬚ Hollow** to auto-optimize, then **🎨 Mint this model as NFT**.

A built-in **21-step tour** runs on first open (Next / Skip) — this manual is the full reference.

---

## 1. Top bar

| Button | Shortcut | What it does |
|---|---|---|
| **↶ Undo** | `Ctrl+Z` | Step one action back. |
| **↷ Redo** | `Ctrl+Y` | Re-apply an undone action. |
| **⤢ Resize canvas** | — | Grow or crop the working grid; the model is kept via an anchor. |
| **🎬 Render studio** | — | Open the full-screen Render Studio (lighting, backgrounds, filters, 4K export). |
| **▶ Play mode** | `P` | Walk your model in first/third person — gravity, AABB collisions, WASD + Space. |

---

## 2. Interaction mode — what a click does

| Mode | Shortcut | What it does |
|---|---|---|
| **Add** | `T` / `A` | Place a voxel on the face you point at. |
| **Erase** | `R` / `E` | Delete the voxel you point at. |
| **Paint** | `G` | Recolour a voxel without changing geometry. |

**Paint bucket** (with Paint active):
- **Plane** — click a voxel to recolour the whole coplanar slice at that depth.
- **Colour** — recolour every voxel sharing that colour.
- **All** — recolour the entire model.

---

## 3. Brushes — the shape of each stroke

| Brush | Shortcut | What it does |
|---|---|---|
| **Single** | `V` / `1` | One 1×1×1 voxel per click; drag paints a trail. |
| **Face** | `F` / `2` | 2D flood-fill on the clicked face — extrudes or erases the whole coplanar surface. |
| **Box** | `B` / `3` | Drag corner-to-corner to fill or clear a rectangular prism. |
| **Line** | `L` / `4` | Draw / paint / erase a 3D voxel line between two clicks (Bresenham). |
| **Plane** | — | Fill the entire grid plane at the clicked depth (whole slice). |
| **Void** | — | Flood the connected empty region you click (3D bucket-fill of empty space). |
| **Pick** | — | Pointer-select: click voxels one by one, then `Del` to remove — the easy hand-pick delete. |
| **Sphere** | `5` | Erase all voxels within a radius of the click. |
| **Square** | `6` | Stamp a filled square (side = 2×radius) on the pointed plane. |
| **Circle** | `C` / `7` | Stamp a filled disc (radius from the slider). |
| **Solid** | `8` | Stamp a filled 3D shape (sphere/cube/cylinder/cone/pyramid/octahedron); Erase carves it. |

**Radius** slider and **Shape** dropdown set the size/geometry for the Sphere/Square/Circle/Solid brushes.

---

## 4. Surface volume

| Button | Shortcut | What it does |
|---|---|---|
| **▣ Grow** | `+` | Add one voxel layer on every exposed face — inflates/thickens the model. |
| **▢ Shrink** | `-` | Peel one voxel layer off every exposed face — erodes the model. |
| **⬚ Hollow (auto-optimize)** | — | Remove every voxel fully hidden inside the model. Looks identical, far lighter, **much cheaper to mint**. Always run this before minting. |

---

## 5. Layers

Work on independent layers; hide or delete them separately. New voxels land on the **active** layer.

| Button | What it does |
|---|---|
| **＋ Add layer** | Create a new layer (auto-named, never duplicated). |
| **－ Remove** | Delete the active layer and all its voxels (keeps at least one). |
| 👁 / 🚫 | Toggle a layer's visibility. Click a row to make it active. |

---

## 6. Selection & transform

| Tool | Shortcut | What it does |
|---|---|---|
| **Wand — by colour** | `W` | Select every voxel connected to the click sharing its colour. |
| **Wand — same colour (whole model)** | `Shift+W` | Select every voxel of that colour across the whole model. |
| **Select — by face** | `U` | Select the contiguous coplanar same-colour face/region you click. |
| **Wand — by shape** | `J` | Select the whole connected solid, ignoring colour. |
| **Marquee (dotted box)** | `K` | Drag a dotted rectangle to select everything inside. |
| **Select all** | `Ctrl+A` | Select every voxel. |
| **Clear selection** | `Esc` | Deselect everything. |
| **Move the selection** | `M` | X/Y/Z gizmo to translate (snaps to grid). Shift-drag duplicates. |
| **Rotate X / Y / Z 90°** | — | Rotate the selection 90° around that axis. |
| **Duplicate** | `Shift+D` | Copy the selection in place; move it with the gizmo. |
| **Delete selection** | `Del` | Remove all selected voxels. |
| **Clear scene** | — | Delete every voxel and start over. |

---

## 7. Palette & colour editing (right panel)

| Control | What it does |
|---|---|
| **Active colour** | The colour used by Add and Paint. Pick any RGB. |
| **Add swatch** | Save the current colour into the palette. |
| **Ready colours** | Click a chip to set the active colour. **Alt+click** a voxel = eyedropper (picks its colour). |
| **Recolour selection** | Paint every selected voxel with the active colour. |
| **Hue / Saturation / Lightness** | Fine-tune the active colour. **Reset sliders** restores them. |

> 💡 More colours & detail increase the on-chain mint price. Start with the **smallest canvas** to build cheaply.

---

## 8. Go to (right panel)

| Button | What it does |
|---|---|
| **🏠 Home** | Visit this room in first person. |
| **Explore** | Stand in front of this gem in Lost Pixel City. |
| **🗺 Map** | Open the public voxel map (`lpg-map`). |

---

## 9. Merge & Voxelizer

![Voxelizer window](docs/img/07-voxelizer.png)

| Tool | What it does |
|---|---|
| **∪ Union** | Import a `.vox` and add its voxels (boolean union). |
| **∖ Subtract** | Import a `.vox` and remove any scene voxels it overlaps. |
| **🧊 Open the Voxelizer** | Import `.obj/.glb/.gltf/.stl/.ply` or an image (jpg/png), **or generate free AI art**, and convert it to voxel art fitted to your canvas. Oversize imports trigger a warning and auto-fit. |

---

## 10. Render Studio

![Render Studio](docs/img/06-render-studio.png)

A full-screen studio to compose a scene shot — **non-destructive**, it never changes your voxels. You can **orbit the model live** inside it, and the grid + canvas bounds disappear so only the voxels are the scene.

- **Lighting scheme** — Studio · Soft · Dramatic · Night · Sunset · Neon · Midday, with a **Light power** slider.
- **Filters (stackable)** — Glitch · Colour · Shadows · Lighting · Levels · Pixelate · Deep-blue · Noise · LEGO, with a **Colour mix** slider.
- **Background image** and **Base / floor image** — drop a PNG behind the model (the renderer is transparent so it shows through).
- **Overlay image planes** — add images that sit **in front of or behind** the model (Paint-3D style); send forward/back with ⬆/⬇.
- **Aspect** — Free / 1:1 / 16:9 / 9:16 / 4:3.
- **⬇ Export frame (4K)** — composite bg + planes + model + filters into a 4K PNG.

---

## 11. Export

| Button | Format |
|---|---|
| **.vox** | MagicaVoxel — round-trips with MagicaVoxel / VoxEdit / Goxel. |
| **.glb** | glTF binary, greedy-meshed. |
| **.obj** | Wavefront OBJ + MTL, greedy-meshed with per-quad colours. |

---

## 12. Publish to the map & mint

| Button | What it does |
|---|---|
| **➕ Add to public map (1:1)** | Publish the model onto the 8000×256 public map at exact 1:1 voxel resolution. Owner-locked. |
| **🌍 Send gem room to the map** | Publish this gem's room onto the public map as its LAND. |
| **🗺 Save & lock position (wallet)** | Optional. Adding to the map is FREE; connect a wallet only to SAVE/PIN the position on-chain. |
| **🎨 Mint this model as NFT** | Open the mint modal. |

### Mint flow (fully on-chain)

1. Click **🎨 Mint this model as NFT**.
2. Review the preview: voxel count, dimensions, size class, on-chain KB and estimated gas.
3. **Pick the face** (0–5) that becomes the SVG thumbnail — you see all 6 face previews.
4. Name it, connect your wallet, accept if it's a heavy model.
5. **🔥 Burn PIXELS & mint** — minting burns PIXELS by size (32³=1, 64³=2, 128³=3, 256³=6). Name & voxels are **immutable forever**.
6. After minting: **place it on the map** or **visit the public map**.

> ⛽ **Lower your gas fee:** ⬚ Hollow the model, use fewer colours and less detail, and pick the smallest canvas — fewer voxels = a smaller on-chain payload = cheaper mint.

---

## 13. Keyboard shortcuts

| Key | Action | Key | Action |
|---|---|---|---|
| `Ctrl+Z` / `Ctrl+Y` | Undo / Redo | `W` / `Shift+W` | Wand by colour / whole model |
| `T`/`A` · `R`/`E` · `G` | Add · Erase · Paint | `U` · `J` · `K` | Face · Shape · Marquee select |
| `V`/`1` · `F`/`2` · `B`/`3` | Single · Face · Box | `Ctrl+A` · `Esc` | Select all · Clear |
| `L`/`4` | Line | `M` · `Shift+D` · `Del` | Move · Duplicate · Delete |
| `5` · `6` · `C`/`7` · `8` | Sphere · Square · Circle · Solid | `+` / `-` | Grow / Shrink |
| `P` | Play mode | | |

---

## 14. Pro tips

- **Build cheap, then detail.** Start 32³; only scale up when the silhouette is right.
- **Always Hollow before minting** — interiors are invisible dead weight that cost gas.
- **Use layers** to isolate parts (e.g. body vs. accessories) and hide them while editing.
- **Eyedropper** (Alt+click) keeps your palette consistent.
- **Render Studio is non-destructive** — experiment freely; it never alters your model.

---

*See also: `WEB3-PROTOCOL.md` (contracts) and `STREAMING-PIXELS.md` (rewards). Source: `voxel-studio.html`.*
