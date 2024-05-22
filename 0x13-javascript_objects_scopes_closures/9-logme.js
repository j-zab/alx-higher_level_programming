#!/usr/bin/node
/**
 * A funct th@ prints the # of args already printed and the new arg val
 */
let counter = 0;

exports.logMe = function count (item) {
  console.log(`${counter}: ${item}`);
  counter += 1;
};
