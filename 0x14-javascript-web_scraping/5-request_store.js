#!/usr/bin/node
const req = require('request');
const fs = require('fs');
const allArgs = process.argv.slice(2);
const fn = allArgs[1];
const url = allArgs[0];

req.get(url, (err, r, cont) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fn, cont, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
