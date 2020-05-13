#!/usr/bin/node
// Let there be comments
const req = require('request');
const allArgs = process.argv.slice(2);
const url = allArgs[0];

req.get(url, function (err, r, cont) {
  if (err) {
    console.log(err);
  } else {
    let op = {};
    let init = 0;
    const tmp = JSON.parse(cont);
    const len = tmp.length;
    while (init < len) {
      if (tmp[init].completed) {
        if (!(tmp[init].userId in op)) {
          op[tmp[init].userId] = 0;
        }
        op[tmp[init].userId] += 1;
      }
      init += 1;
    }
    console.log(op);
  }
});
