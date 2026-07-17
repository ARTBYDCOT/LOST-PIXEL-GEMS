# Public Math, Formulas & Programming Commands

Full public disclosure of the mathematics, algorithms, shaders, and image-tracing used across Lost Pixel Gems. Nothing here is hidden — the world is built from these formulas.

## 1. World layout math

**Honeycomb (colmena) grid** — odd rows offset half a cell:
```
x = (col − (COLS−1)/2) · HEX  +  (row odd ? HEX/2 : 0)
z = (row − (ROWS−1)/2) · HEX · 0.87
```

**Phyllotaxis (sunflower) spiral** — the alternate "one unique spiral" layout:
```
GOLDEN = π · (3 − √5)  ≈ 2.39996 rad      // golden angle
r(i)   = PITCH · √(i + 0.5)
θ(i)   = i · GOLDEN
x = r·cos θ ,  z = r·sin θ
PITCH  = HEX / 1.9        // → nearest-neighbour spacing ≈ HEX
```

**3-row grid** (low-noise layout): `col = ⌊i/3⌋, row = i mod 3`.

## 2. Terrain (radial mountains around a flat valley)
```
r = √(x² + z²)
if r ≤ CITY_RADIUS:  height = 0                         // flat meadow
else:
  t = r − CITY_RADIUS
  height = max(0, 1.35·t + 150·sin(0.0032x) + 95·cos(0.0016z) + 80·sin(0.0014(x+z)))
```

## 3. Voxel ↔ world scale
```
VOX_GRID = 250                    // editable grid per parcel
VOX_UNIT = VOX_SIDE / VOX_GRID    // world units per voxel
VOX_MAXH = VOX_H · VOX_UNIT       // build-height ceiling (VOX_H = 69)
model scale sc = TARGET_FOOTPRINT / max(bbox.x, bbox.z)   // uniform → true proportions
```

## 4. `.vox` format & the z-up → y-up swap
MagicaVoxel chunks: `MAIN` (container) → `SIZE`, `XYZI` (x,y,z,colorIndex), `RGBA` (256 palette).
MagicaVoxel is **Z-up**; three.js is **Y-up**, so:
```
editorX = voxX ,  editorY = voxZ ,  editorZ = voxY      // import
voxX = editorX ,  voxY = editorZ ,  voxZ = editorY      // export (writeVox)
```

## 5. Greedy meshing (mesh optimization)
For each of the 3 axes, for each slice, build a mask of same-color faces and **merge maximal rectangles** into single quads — reduces a 356k-voxel model from millions of triangles to ~18k. This is why big voxel art stays web-light.

## 6. Portal vortex — GLSL swirl (per-gem unique)
```glsl
uniform float uTime, uSeed, uArms, uSpeed, uTwist; uniform vec3 uColor; varying vec2 vUv;
void main(){
  vec2 p = vUv - 0.5; float r = length(p); float a = atan(p.y, p.x);
  float sw   = sin(a*uArms + uTime*uSpeed + uSeed - r*uTwist);
  float glow = smoothstep(0.5, 0.03, r);
  vec3  col  = mix(vec3(0.03,0.05,0.12), uColor, 0.5+0.5*sw) * glow;
  gl_FragColor = vec4(col, glow);
}
```
Per portal `i`: `uSeed = (i·2.39996) mod 2π`, `uArms = 2 + i mod 5`, `uTwist = 15 + 3·(i mod 6)`, `uSpeed` alternates sign — so all 111 spirals differ.

## 7. Deflationary burn formula
```
PIXELS_burned(V) = ceil(V · rate(V))          // V = voxel count
rate: 0.10 (≤1k) · 0.08 (≤10k) · 0.06 (≤100k) · 0.05 (≤356k)   // regressive per-voxel
supply(t) = supply(0) − Σ PIXELS_burned(V_i)  // monotonically decreasing
```
Universe target: **8,000,000 voxels** on an 8000×256 map.

## 8. Image tracing (trazado de imagen)
- **Ground decals:** each gem's 44×44 PNG thumbnail is used directly — its **alpha channel is the silhouette**, so `alphaTest` traces the gem's shape onto the ground with no extra extraction.
- **Vox thumbnails:** pre-rendered `assets/vox-render/{id}.png` billboards trace each gem's model at a distance (cheap LOD).
- **OG/social cards:** 1200×630 images rendered from a JSX/HTML social card → SVG (satori) → PNG (resvg).

## 9. Programming commands (the moving parts)
```js
// instanced world objects (1 draw call each): portals, buildings, vegetation, ruins
new THREE.InstancedMesh(geo, mat, N);  inst.setMatrixAt(i, m4);  inst.instanceColor = ...
// AABB physics (city + play mode): per-axis integrate then resolve collision
p.x += v.x·dt; if (collides) { p.x -= v.x·dt; v.x = 0 }   // repeat for y,z
// animation: rigged playback
mixer = new THREE.AnimationMixer(model); mixer.clipAction(walk).play(); mixer.update(dt)
```

**Public Map API** (Node or PHP, identical contract):
```
GET  /api/placements            → all models on the map
GET  /api/placement?token_id=N  → one (with vox payload)
POST /api/place    {token_id, owner, name, x, z, rot, vox_b64}   // owner-gated
POST /api/move     {token_id, owner, x, z, rot}                  // locked → owner only
POST /api/remove   {token_id, owner}                             // owner only
POST /api/lock     {token_id, owner, newOwner}                   // pin position
```

All of the above is in the source in this repo — read it, verify it, improve it.
