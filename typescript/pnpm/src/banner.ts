// CLI banner helper, migrated to chalk v5.
//
// chalk v5 is pure ESM. Under Node's require(esm) support (Node 22.12+) the
// CommonJS build can still `require('chalk')` and esModuleInterop resolves the
// default export, so no ESM conversion is needed here. The only API break is
// the removal of `chalk.keyword()` (see warn() below).
import chalk from 'chalk';

export function banner(text: string): string {
  // chalk v4 chained API.
  return chalk.bold.green(text);
}

export function warn(text: string): string {
  // chalk v5 removed .keyword(); 'orange' (RGB 255,165,0) maps to chalk.hex('#FFA500').
  return chalk.hex('#FFA500')(text);
}

export function plain(text: string): string {
  return chalk.reset(text);
}
