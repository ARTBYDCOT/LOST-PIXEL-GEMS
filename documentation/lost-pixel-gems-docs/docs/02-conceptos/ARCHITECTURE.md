# Architecture

**Static-first, server-optional, chain-of-truth.**

```
Browser (three.js apps) ──► public RPC (read-only: balanceOf/ownerOf)
        │
        └──► Public Map API (Node or PHP) ──► SQLite (placements cache)
                                                   ▲
                    On-chain contracts ────────────┘  (source of truth once deployed)
```

- **web/** — all pages are static HTML + JS (three.js r128). No build step.
- **server/** — the *only* server is the public-map placement API. Two drop-in
  implementations: `node/` (Node + better-sqlite3) and `php/` (PHP + PDO SQLite).
- **contracts/** — the chain is the durable archive; the map is rebuildable from
  contract data alone (server independence is a design goal).
- **No secrets in the client.** Wallet writes are user-signed; reads use public RPC.
