#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  let init = 0;
  for (init = 0; init < x; init++) {
    func();
  }
};
