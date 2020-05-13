#!/usr/bin/node
// Let there be comments
const req = require('request');
const allArgs = process.argv.slice(2);
const url = allArgs[0];

req.get(url, function (err, r, cont) {
  if (err) {
    console.log(err);
  } else {
    let i = 0;
    let j = 0;
    let cnt = 0;
    const films = JSON.parse(cont).results;
    const filmsLen = films.length;
    while (i < filmsLen) {
      const chars = films[i].characters;
      const charsLen = chars.length;
      while (j < charsLen) {
        if (chars[j].includes('/18/')) {
          cnt += 1;
        }
        j += 1;
      }
      i += 1;
    }
    console.log(cnt);
  }
});
