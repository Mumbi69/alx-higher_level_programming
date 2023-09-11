#!/usr/bin/node
const { argv } = require('process');

if (!isNaN(argv[2])) {
  for (let m = 0; m < parseInt(argv[2]); m++) {
    let row = '';
    for (let s = 0; s < parseInt(argv[2]); s++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
