#!/usr/bin/node

const numx = parseInt(process.argv[2]);
if (isNaN(numx)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < numx; i++) {
    console.log('C is fun');
  }
}
