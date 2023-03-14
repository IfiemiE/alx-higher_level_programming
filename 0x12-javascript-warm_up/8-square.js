#!/usr/bin/node

const numx = parseInt(process.argv[2]);
if (isNaN(numx)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numx; i++) {
    let stars = '';
    for (let j = 0; j < numx; j++) {
      stars += 'X';
    }
    console.log(stars);
  }
}
