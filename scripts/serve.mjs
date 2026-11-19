import {createServer} from 'node:http';
import {createReadStream, statSync} from 'node:fs';
import {extname, resolve, sep} from 'node:path';

const root = resolve(process.env.CATALOGUE_ROOT || '_site');
const base = (process.env.CATALOGUE_BASE || '').replace(/\/$/, '');
const types = {'.html':'text/html', '.mjs':'text/javascript', '.js':'text/javascript', '.css':'text/css', '.wasm':'application/wasm', '.json':'application/json', '.md':'text/plain'};
createServer((req, res) => {
  try {
    const urlPath = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (base && !urlPath.startsWith(base + '/')) throw new Error('Path outside catalogue');
    const pathname = urlPath.slice(base.length);
    const path = resolve(root, '.' + (pathname === '/' ? '/index.html' : pathname));
    if (!path.startsWith(root + sep)) throw new Error('Path outside catalogue');
    const info = statSync(path);
    if (!info.isFile()) throw new Error('Not a file');
    let start = 0;
    let end = info.size - 1;
    let status = 200;
    const range = req.headers.range?.match(/^bytes=(\d+)-(\d*)$/);
    if (range) {
      start = Number(range[1]);
      end = range[2] ? Math.min(end, Number(range[2])) : end;
      if (end < start) return res.writeHead(416, {'Content-Range': `bytes */${info.size}`}).end();
      res.setHeader('Content-Range', `bytes ${start}-${end}/${info.size}`);
      status = 206;
    }
    res.writeHead(status, {'Accept-Ranges':'bytes', 'Cache-Control':'public, max-age=3600', 'Content-Length':end-start+1, 'Content-Type':types[extname(path)] || 'application/octet-stream'});
    if (req.method === 'HEAD') return res.end();
    createReadStream(path, {start, end}).pipe(res);
  } catch {
    res.writeHead(404).end('File not found');
  }
}).listen(Number(process.env.PORT || 8339), '127.0.0.1', () => console.log('http://127.0.0.1:' + (process.env.PORT || 8339) + base + '/'));
