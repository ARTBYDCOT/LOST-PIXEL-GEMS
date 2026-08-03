# Contributing

Everything here is **CC0** — public domain. You can fork, remix, and ship without asking.

## Ways to contribute
- **Build on the open map.** Read a region on‑chain and embed it (see [docs/MAP.md](./docs/MAP.md)). Share what you make.
- **Write a decoder.** Region/voxel RLE decoders in any language are welcome.
- **Add code examples.** More stacks (Rust/alloy, Go, Swift) in [docs/CODE-EXAMPLES.md](./docs/CODE-EXAMPLES.md).
- **Build an ERC‑8257 tool** for the ecosystem and register it (see [docs/AGENTS.md](./docs/AGENTS.md)).
- **Improve docs.** Fixes, clarifications, diagrams.

## Ground rules
- Keep it **on‑chain and host‑agnostic** — no manual `.htaccess`, no hard‑coded hosts in front‑ends; read galleries from chain.
- **No secrets in client code.** All signing is user‑side.
- **Verify addresses** against [docs/CONTRACTS.md](./docs/CONTRACTS.md) before wiring anything.
- License your contribution as **CC0** to match the repo.

## Dev pointers
- Contracts registry (machine‑readable): [`contracts.json`](./contracts.json).
- Agent gateway API: [docs/API.md](./docs/API.md).
- Wallet/signing: [docs/WALLET.md](./docs/WALLET.md).

## Reporting
Open an issue with the contract/tool address, chain, tx hash (if any), and steps to reproduce.
