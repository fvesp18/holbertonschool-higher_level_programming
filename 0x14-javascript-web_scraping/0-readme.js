#!/usr/bin/node
const allArgs = process.argv.slice(2);
const fs = require('fs');
const fn = allArgs[0];

fs.open(fn,'r', (err, fd) => {
	if (err) {
		console.log(err);
	} else {
		fs.readFile(fn, 'utf-8', (err, cont) => {
			if (err) {
				return console.log(err);
			} else {
				console.log(cont);
			}
		});
	}
});
