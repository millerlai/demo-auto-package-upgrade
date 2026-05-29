'use strict';

const test = require('node:test');
const assert = require('node:assert');
const { combine, makeClient } = require('../src/fetcher');

test('combine aggregates response data via axios.all/spread', async () => {
  const data = await combine([
    Promise.resolve({ data: 1 }),
    Promise.resolve({ data: 2 }),
  ]);
  assert.deepStrictEqual(data, [1, 2]);
});

test('makeClient applies the function paramsSerializer', () => {
  const client = makeClient('https://api.example.com');
  const serialize = client.defaults.paramsSerializer;
  assert.strictEqual(typeof serialize, 'function');
  assert.strictEqual(serialize({ a: 1, b: 'x y' }), 'a=1&b=x%20y');
});
