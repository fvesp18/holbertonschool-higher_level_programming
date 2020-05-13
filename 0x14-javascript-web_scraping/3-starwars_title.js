#!/usr/bin/node
const req = require('request');
const allArgs = process.argv.slice(2);
const id = allArgs[0];
const url = 'https://swapi-api.hbtn.io/api/films/';

req.get(url + id, (err, r, cont) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(cont).title);
  }
});
