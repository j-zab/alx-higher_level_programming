#!/usr/bin/node
/**
 * A funct th@ converts a # from base 10
 * to another base passed as args
 */
exports.converter = function (base) {
  function myConverter (n) {
    return n.toString(base);
  }

  return myConverter;
};
