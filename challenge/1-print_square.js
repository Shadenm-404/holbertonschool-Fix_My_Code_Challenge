#!/usr/bin/node

const size = parseInt(process.argv[2], 10);

if (isNaN(size) || size <= 0) {
  process.exit(0);
}

for (let row = 0; row < size; row++) {
  console.log("#".repeat(size));
}
