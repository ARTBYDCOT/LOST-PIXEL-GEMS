# Deploy

## Static site (any host, incl. shared/PHP hosting or GitHub Pages)
Upload `web/` to your web root. Open `index.html`. Done.

## Public map — pick one backend
### Node
    cd server/node && npm install && PORT=3000 node server.js   # pm2 for permanence
### PHP (shared hosting, no Node)
    Copy server/php/ into your web root as /map/ ; ensure PDO SQLite + mod_rewrite.
    Make the folder writable so it can create map.db.

Same-origin hosting (map served from your domain) avoids CORS/mixed-content.
