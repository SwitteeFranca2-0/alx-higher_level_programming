#!/usr/bin/node

let i = 0;
let b = 0;
let square = '';
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    for (b = 0; b < process.argv[2]; b++) {
      square += 'X';
    }
    if (i !== parseInt(process.argv[2]) - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
