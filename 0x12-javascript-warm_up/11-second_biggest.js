#!/usr/bin/node

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(0);
} else {
  const arrNum = process.argv;
  let maxNum = parseInt(arrNum[2]);
  for (let i = 2; i < arrNum.length; i++) {
    arrNum[i] = parseInt(arrNum[i]);
    if (arrNum[i] > maxNum) {
      const swap = arrNum[i];
      arrNum[i] = maxNum;
      maxNum = swap;
    }
  }
  let secMax = arrNum[2];
  for (let i = 2; i < arrNum.length; i++) {
    if ((arrNum[i] > secMax) && (arrNum[i] !== maxNum)) {
      const swap = secMax;
      secMax = arrNum[i];
      arrNum[i] = swap;
    }
  }
  console.log(secMax);
}
