#!/usr/bin/node
const allArgs = process.argv.slice(2);
const fs = require('fs');
const fn = allArgs[0];
const str = allArgs[1];

console.log(str);

fs.writeFile(fn, str, (err, fd) => {
  if (err) {
    console.log(err);
  }
});
