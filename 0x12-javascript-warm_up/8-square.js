#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let line = '';
    for (let j = 0; j < num; j++) {
      line = line + 'X';
    }
    console.log(line);
  }
}
