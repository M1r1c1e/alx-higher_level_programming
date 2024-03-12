#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const sortedlist = list.filter((currentElement) => currentElement === searchElement);
  return sortedlist.length;
};
