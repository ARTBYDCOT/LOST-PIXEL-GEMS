# Creation Tools for Artists — free & open

Lost Pixel Gems ships a growing suite of **free creation tools** so **any artist** can build for the shared world — no cost to create, no lock-in. Art is by **D.C.O.T. and anyone who contributes**, and so are the tools.

## Available now

| Tool | What it does | Where | Cost |
|---|---|---|---|
| **Voxel Editor** | Full MagicaVoxel-style 3D voxel editor in the browser — brushes, geometric shapes, selection & marquee, color-by-shape/wand, layers, 3D gizmo (move/rotate/scale), grow/shrink, AI shape prompts, undo/redo, autosave | `voxel-studio.html` | Free |
| **Gem-room mode** | Open `?gem=N` → the gem's model loads 1:1 in a 250×250×69 canvas, palette-locked, per-gem autosave | `voxel-studio.html?gem=N` | Free |
| **Multi-format import** | Merge/union/subtract `.vox`; place uploaded **`.obj / .glb / .gltf / .vrm / .vox`** into the world | editor + city uploader | Free |
| **Export** | `.vox` (MagicaVoxel), `.glb` & `.obj` (greedy-meshed to cut polygons) | editor | Free |
| **In-app editing & animation** | Edit *and* animate right inside the app — rigged model playback (AnimationMixer / Walk clips), play-mode with gravity & collisions, and live-preview of changes as you build | editor + room | Free |
| **First-person room / spectator** | Walk any model in play mode — mirrors live edits | `room.html` | Free |
| **vox → web mesh pipeline** | Pure-Python greedy mesher (`.vox` → optimized `.glb`) | `tools/` | Free |

**Free to draft, always.** Creating and exporting never costs anything. The only on-chain cost is **making a construction permanent** (burning PIXELS), per the [economy](ECONOMY.md).

## Roadmap — coming tools

| Tool | Description | Status |
|---|---|---|
| **🎨 Pixel Art Studio** | A dedicated **2D pixel-art tool** for artists — draw sprites/tiles, palettes, animation frames, and export straight into the LPG pipeline | Planned |
| **`.vox/.obj/.glb → SVG / interactive-HTML` viewer** | Self-contained, embeddable model viewer with buttons + info (V2-referenced) | In progress |
| **On-chain save** | Sign a metadata tx to commit a room/model fully on-chain | With contracts ([CONTRACTS.md](CONTRACTS.md)) |
| **Collaborator parcels** | Owners grant edit rights on parcels/quadrants | Planned |

## Philosophy
- **Free to create** — the tools are for everyone, not gated behind tokens.
- **Open source** — fork the editor, improve it, ship your own.
- **Interoperable** — standard formats in and out (`.vox`, `.obj`, `.glb`, `.gltf`, `.vrm`).
- **Optimized** — greedy meshing keeps big voxel art light enough for the web.

Contributions to the tools (and the upcoming Pixel Art Studio) are welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).
