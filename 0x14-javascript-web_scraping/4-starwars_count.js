#!/usr/bin/node
// Let there be comments
const req = require('request');
const allArgs = process.argv.slice(2);
const url = allArgs[0];

req.get(url, (err, resp, cont) => {
  if (err) {
    console.log(err);
  } else {
    let cnt = 0;
    const films = JSON.parse(cont).results;
    for (const lol of films) {
      const chars = lol.characters;
      for (const lmao of chars) {
        if (lmao.includes('18')) {
          cnt += 1;
        }
      }
    }
    console.log(cnt);
  }
});
