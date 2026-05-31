'use strict';

const test = require('node:test');
const assert = require('node:assert');
const http = require('node:http');
const { createSession, get, cookieString } = require('../src/client');

// Spin up a throwaway local server so the test is deterministic and offline.
function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      res.setHeader('Set-Cookie', 'sid=abc123; Path=/');
      res.end('ok');
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

test('request fetches through the cookie jar', async () => {
  const server = await startServer();
  const { port } = server.address();
  const url = `http://127.0.0.1:${port}/`;
  try {
    const jar = createSession();
    const res = await get(jar, url);
    assert.strictEqual(res.status, 200);
    assert.strictEqual(res.body, 'ok');
  } finally {
    server.close();
  }
});

test('the tough-cookie jar captures the Set-Cookie header', async () => {
  const server = await startServer();
  const { port } = server.address();
  const url = `http://127.0.0.1:${port}/`;
  try {
    const jar = createSession();
    await get(jar, url);
    // The cookie the server set is now stored by tough-cookie — the
    // transitive dependency the main program never imports directly.
    assert.match(cookieString(jar, url), /sid=abc123/);
  } finally {
    server.close();
  }
});
