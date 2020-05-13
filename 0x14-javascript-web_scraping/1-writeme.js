#!/usr/bin/node
const allArgs = process.argv.slice(2);
const fs = require('fs');
const fn = allArgs[0];
const str = allArgs[1];

fs.writeFile(fn, str, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
