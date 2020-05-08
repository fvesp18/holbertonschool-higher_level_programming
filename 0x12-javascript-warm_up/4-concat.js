#!/usr/bin/node
const allArgs = process.argv.slice(2);
const length = allArgs.length;
const first = allArgs[0];
const word = ' is ';
const second = allArgs[1];

if (length > 1) {
  const str = first.concat(word).concat(second);
  console.log(str);
} else if (allArgs[1] === undefined && allArgs[0] !== undefined) {
  const str = first.concat(word).concat(undefined);
  console.log(str);
} else if (length === 0) {
  console.log('undefined is undefined');
}
