#!/usr/bin/node
// Add a comment lmfao
exports.converter = function (base) {
  if (base === 10) {
    return function (base) {
      return base.toString(10);
    };
  } else {
    return function (base) {
      return base.toString(16);
    };
  }
};
