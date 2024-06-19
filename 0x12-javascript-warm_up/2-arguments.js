#!/usr/bin/node
const count = process.argv.length;
console.log(count === 2 ? 'No Argument' : count === 3 ? 'Argument found' : 'Arguments found');
