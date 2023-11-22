#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 0 || a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
