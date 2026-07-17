# How to Use the Contracts Directory

## Overview
Each smart contract in Lost Pixel Gems has a dedicated folder with two subdirectories:

- **`/art`** - Artwork and design assets for public backup storage
- **`/docs`** - Technical documentation and specifications

---

## Structure

```
contracts/
├── 01-LPG-V1/
│   ├── art/              ← Upload artwork here
│   ├── docs/             ← Upload technical docs here
│   └── README.md         ← Contract overview
│
├── 02-LPG-V2-LPGNTRCTV/
│   ├── art/
│   ├── docs/
│   └── README.md
│
├── [... remaining contracts ...]
│
└── INDEX.md              ← Master index of all contracts
```

---

## Usage Instructions

### Adding Artwork to a Contract

1. **Navigate** to the contract folder
   - Example: `docs/02-conceptos/contracts/01-LPG-V1/`

2. **Place artwork in `/art` folder**
   - Formats: PNG, JPG, SVG, GIF, WebP
   - Naming convention: descriptive kebab-case (e.g., `gem-design-01.png`)

3. **Update the contract's README.md**
   - Add artwork references in the "Resources" section

### Adding Documentation to a Contract

1. **Navigate** to the contract folder
   - Example: `docs/02-conceptos/contracts/07-PIXELS-ERC20/`

2. **Create markdown files in `/docs` folder**
   - Naming convention: descriptive kebab-case (e.g., `burn-mechanism-spec.md`)

3. **Link from README.md**
   - Reference documentation in the main README

---

## Contract Folder Reference

### Live Collections
| Folder | Name | Purpose |
|--------|------|---------|
| `01-LPG-V1` | The 111 Gems | Genesis collection |
| `02-LPG-V2-LPGNTRCTV` | Companion Collection | Extended ecosystem |
| `03-LPL` | Community Collection | Ecosystem participation |
| `04-LPGR` | Infrastructure | Supporting infrastructure |
| `05-LPC-BOT-BOTTT` | Avatar/Bot Tier | Interactive features |
| `06-ABS` | Ecosystem Component | Core infrastructure |

### Protocol Contracts
| Folder | Name | Type | Status |
|--------|------|------|--------|
| `07-PIXELS-ERC20` | Native Token | ERC-20 | Open for Audit |
| `08-VoxelLAND-ERC721` | Map Construction | ERC-721 | Open for Audit |
| `09-MapArchive` | On-Chain History | Archive | Open for Audit |
| `10-Exhibition` | NFT Display | View-Only | Open for Audit |

---

## File Organization Best Practices

### Artwork Files
```
/art/
├── designs/
│   ├── concept-01.png
│   ├── concept-02.png
│   └── [...]
├── renders/
│   ├── render-final.png
│   └── [...]
└── references/
    └── [...]
```

### Documentation Files
```
/docs/
├── technical-specification.md
├── audit-notes.md
├── implementation-guide.md
└── [...]
```

---

## Accessing the Master Index

**Location:** `docs/02-conceptos/contracts/INDEX.md`

The INDEX.md file provides:
- Quick reference to all contracts
- Links to individual contract folders
- Categorization by purpose and type
- Integration guidelines for developers

---

## Public Backup Notes

- All artwork is stored for **public backup and archival purposes**
- Files in `/art` folders are publicly accessible
- No private or sensitive information should be stored in contract folders
- Use `/docs` for public technical documentation only

---

## Questions or Issues?

- See individual contract README.md files for specific details
- Check [CONTRACTS.md](../CONTRACTS.md) for original specifications
- Review [SECURITY.md](../SECURITY.md) for audit procedures

---

**Last Updated:** 2026  
**Language:** English  
**Status:** Ready for public use
