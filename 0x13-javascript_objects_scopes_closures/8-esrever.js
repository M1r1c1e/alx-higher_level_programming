#!/usr/bin/node
exports.esrever = function (list) {
  const reversedElem = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedElem.push(list[i]);
  }
  return reversedElem;
};
