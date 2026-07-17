# Voxel Editor — functions, limits & comparison

Full, public disclosure of what the **LPG Voxel Editor** (`voxel-studio.html`) can and cannot do, and how it compares to the main voxel-art editors/engines online. We publish this openly so artists know exactly what they're working with.

## Functions (LPG Voxel Editor)

| Category | Functions |
|---|---|
| **Placement** | Add / erase / paint voxels; box, line, plane, sphere, cylinder shapes |
| **Selection** | Wand by color, wand by shape, dotted marquee box-select; move/duplicate selection via 3D gizmo |
| **Transform** | 3D gizmo: move · rotate · scale; grow / shrink surface; resize canvas 32³ → 256³ |
| **Color** | Editable palette, add swatches, palette-lock (gem rooms), color picker |
| **Layers** | Add / remove / switch layers |
| **AI assist** | Text-prompt shape generator (archetype vocabulary) |
| **Import** | `.vox` union / subtract (boolean merge); place `.obj / .glb / .gltf / .vrm / .vox` |
| **Export** | `.vox` (MagicaVoxel), `.glb`, `.obj` — greedy-meshed to cut polygons |
| **Animation / play** | Play mode (first/third person, gravity, AABB collision); rigged model playback (AnimationMixer / Walk clips) |
| **Persistence** | Per-gem autosave; owner-stamped saves; room mirror shows live edits |
| **On-chain** | Prepare fully-on-chain payload; owner-gated map placement (burn-to-mint, when contracts ship) |
| **Keys** | MagicaVoxel-style shortcuts (T add, R erase, G paint, V/F/B/L/C shapes, M move, +/− grow/shrink) |
| **Platform** | 100% browser, no install; works on PC & mobile (look/orbit) |

## Limits (published honestly)

| Limit | Value | Why |
|---|---|---|
| Max canvas | **256³** (gem rooms fixed at 250×250×69) | Web memory/perf |
| Practical voxel count | up to ~**356k** (a gem "garden"); in-world/room load capped ~**90k–140k** | Browser mesh/draw cost |
| Rendering | three.js r128, greedy meshing | Keeps big art web-light |
| Persistence today | **localStorage** (per browser) | On-chain/shared save ships with the LAND contract |
| Mobile | look/orbit works; full touch **move-pad** WIP | Roadmap |
| Palette | 256 colors (indexed, MagicaVoxel-compatible) | `.vox` format |
| No | UV texturing, path-tracing/render farm, rigging authoring | Out of scope — use desktop tools + import |

## Comparison with the main online voxel editors / engines

| Feature | **LPG Editor** | MagicaVoxel | VoxEdit (Sandbox) | Goxel | Blockbench |
|---|---|---|---|---|---|
| Runs in browser (no install) | ✅ | ❌ (desktop) | ✅ / desktop | ✅ (web build) | ✅ |
| Free | ✅ | ✅ | ✅ | ✅ (open source) | ✅ (open source) |
| Open source | ✅ (MIT) | ❌ | ❌ | ✅ | ✅ |
| Max grid | 256³ | 256³ (2048³ world) | ~model-sized | large | model-sized |
| `.vox` import/export | ✅ | ✅ (native) | partial | ✅ | ✅ |
| `.obj/.glb/.gltf/.vrm` | ✅ import + `.glb/.obj` export | via export | `.glb`/`.vox` | ✅ | ✅ (glTF focus) |
| Greedy-mesh optimization | ✅ | ✅ | ✅ | ✅ | ✅ |
| Animation / play mode | ✅ (play + rigged playback) | ❌ (renders only) | ✅ (rig+anim) | ❌ | ✅ (rig+anim) |
| AI shape assist | ✅ | ❌ | ❌ | ❌ | ❌ |
| Build directly into a shared on-chain world | ✅ | ❌ | ✅ (Sandbox LAND) | ❌ | ❌ |
| Walk the world **as a pixel** | ✅ | ❌ | partial | ❌ | ❌ |
| Deflationary burn-to-mint economy | ✅ (PIXELS) | ❌ | token-based | ❌ | ❌ |

### Honest takeaways
- **Where LPG wins:** zero-install browser tool, **open source (MIT)**, multi-format in/out, **AI assist**, **in-app animation/play**, and — uniquely — **it builds straight into a shared, walkable, on-chain public-art world** with a deflationary economy.
- **Where desktop tools win:** MagicaVoxel is stronger for **pure offline authoring** (bigger worlds, built-in path-traced rendering); VoxEdit/Blockbench have deeper **rig-authoring**. LPG is optimized for **web + world-building + on-chain permanence**, not offline render quality.
- **Recommended flow:** author heavy detail in a desktop tool if you like, then **import `.vox/.obj/.glb`** into the LPG editor to place, animate, and commit into the world.

*Comparisons reflect general capabilities of these tools at time of writing; features evolve — corrections via PR welcome.*
