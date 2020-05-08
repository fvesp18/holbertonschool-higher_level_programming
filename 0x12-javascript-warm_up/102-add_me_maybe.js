#!/usr/bin/node
exports.addMeMaybe = function(num, func) {
	return num + func(num + 1);
};
