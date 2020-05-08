#!/usr/bin/node
const allArgs = process.argv.slice(2);
const length = allArgs.length;
if (length === 0) {
  console.log('No Argument');
} else if (allArgs)  {
  console.log(allArgs[0]);
}
