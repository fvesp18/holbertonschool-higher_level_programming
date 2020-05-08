#!/usr/bin/node
const length = process.argv.slice(2).length;

if (length > 1) {
  const str1 = 'Arguments found';
  console.log(str1);
} else if (length === 1) {
  const str2 = 'Argument found';
  console.log(str2);
} else if (length === 0) {
  const str3 = 'No argument';
  console.log(str3);
}
