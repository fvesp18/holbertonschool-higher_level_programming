#!/usr/bin/node
const allArgs = process.argv.slice(2);
if (allArgs[0] === undefined) {
  console.log('No argument');
} else {
  console.log(allArgs[0]);
}
