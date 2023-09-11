#!/usr/bin/node
if (process.argv.length === 2) {
  console.log("No argument");
} else if (process.argv.length === 3) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
/*
The process.argv variable is like a list (or an array)
that holds all the arguments that were passed to your script
when you started it.
The first item in this list, process.argv[0]
is always the path to the Node.js executable itself.
The second item, process.argv[1], is the path to
JavaScript file that is currently being run.
*/
