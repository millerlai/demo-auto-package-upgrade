// CLI banner helper written against chalk v4 (CommonJS).
//
// chalk v5 is pure ESM, so under this CommonJS tsconfig the default import
// stops resolving (no CJS entry point). Additionally `chalk.keyword()` was
// removed in v5. Both break on upgrade.
import chalk from 'chalk';

export function banner(text: string): string {
  // chalk v4 chained API.
  return chalk.bold.green(text);
}

export function warn(text: string): string {
  // chalk.keyword() exists in v4 but was removed in v5.
  return chalk.keyword('orange')(text);
}

export function plain(text: string): string {
  return chalk.reset(text);
}
