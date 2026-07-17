# 3D Assets

Heavy binaries (`.glb`, full-res `.vox`, ~250 MB) are **not** committed to git.
- The 111 gem rooms come from `.vox` source art (250³ each).
- Web meshes are produced with a pure-Python vox→glb greedy mesher (in `tools/`).
Generate or fetch them into `web/assets/houses/` and `web/assets/vox/` before
running the city/room viewers. The code and pipeline are fully in this repo.
