#!/usr/bin/node

const firstArgument = process.argv[2];

const integerNumber = parseInt(firstArgument);

if (!isNaN(integerNumber)) {
  for (let i = 0; i < integerNumber; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
