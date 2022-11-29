#!/usr/bin/node

let i = 0;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurences');
} else {
  for (; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
