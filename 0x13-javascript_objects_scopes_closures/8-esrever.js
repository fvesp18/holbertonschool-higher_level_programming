#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  let new_list = [];
  for (let i = len; i >= 0; i--) {
    new_list.push(list[i]);
  }
  return new_list;
};
