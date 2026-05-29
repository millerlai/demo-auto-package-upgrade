'use strict';

// Helpers written against the axios 0.27 API.
// `axios.all` and `axios.spread` were removed in axios 1.0, and the
// `paramsSerializer` shape changed from a function to `{ serialize }`.
const axios = require('axios');

// 0.x: axios.all + axios.spread. Removed in 1.x (use Promise.all + destructuring).
function combine(promises) {
  return axios.all(promises).then(
    axios.spread((...responses) => responses.map((r) => r.data))
  );
}

// 0.x: paramsSerializer is a plain function.
// 1.x: must be `{ serialize: (params) => ... }`.
function makeClient(baseURL) {
  return axios.create({
    baseURL,
    paramsSerializer: (params) =>
      Object.entries(params)
        .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
        .join('&'),
  });
}

module.exports = { combine, makeClient };
