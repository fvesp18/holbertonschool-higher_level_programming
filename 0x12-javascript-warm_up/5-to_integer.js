#!/usr/bin/node
const allArgs = process.argv.slice(2);
const str = 'My Number: ';
const str2 = 'Not a number';

if (parseInt(allArgs[0])) {
  console.log(str.concat(parseInt(allArgs[0])));
} else {
  console.log(str2);
}
