#!/usr/bin/node
const allArgs = process.argv.slice(2);
const url = allArgs[0];
const req = require('request');

req.get(url, (err, resp) => {
  if (err || resp) {
    console.log('code:', resp.statusCode);
  }
});
