import test from 'node:test';
import assert from 'node:assert';
import chalk from 'chalk';
import { banner, warn } from '../src/banner';

// Force colour so ANSI codes are emitted even in a non-TTY test runner.
// chalk is a singleton, so this also affects the instance used by banner().
chalk.level = 3;

test('banner wraps text in ANSI codes', () => {
  const out = banner('hi');
  assert.ok(out.includes('hi'));
  // bold = \x1b[1m ; green = \x1b[32m
  assert.match(out, /\x1b\[\d+m/);
});

test('warn uses chalk.keyword', () => {
  const out = warn('careful');
  assert.ok(out.includes('careful'));
});
