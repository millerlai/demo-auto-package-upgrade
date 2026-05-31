'use strict';

// HTTP helpers written against `request@2.88.2` — the package's final,
// *deprecated* release. There is no newer `request` and there never will be.
//
// The main program uses `request` directly and never imports `tough-cookie`.
// Yet every cookie this client stores is handled by `tough-cookie`, which
// `request` pins to `~2.5.0`. tough-cookie < 4.1.3 is vulnerable to prototype
// pollution (CVE-2023-26136). The `~2.5.0` pin blocks the upgrade to 4.1.3+,
// and because `request` is deprecated, no parent release will ever relax it.
//
// This is the "transitive dependency blocked by an unmaintained intermediate"
// case: B (tough-cookie) must move, but A (request) — the only thing the main
// program actually uses — won't let it.
const request = require('request');

// request.jar() builds a tough-cookie CookieJar wrapper under the hood.
function createSession() {
  return request.jar();
}

// Promisified GET that drives the cookie jar and returns { status, body }.
function get(jar, url) {
  return new Promise((resolve, reject) => {
    request.get({ url, jar }, (err, res, body) => {
      if (err) return reject(err);
      resolve({ status: res.statusCode, body });
    });
  });
}

// Read back the cookies tough-cookie stored for a URL. `getCookieString` is
// tough-cookie's API, surfaced here through request's jar wrapper — the only
// way the main program ever touches the transitive dependency.
function cookieString(jar, url) {
  return jar.getCookieString(url);
}

module.exports = { createSession, get, cookieString };
