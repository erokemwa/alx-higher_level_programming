#!/usr/bin/node

// Import the `fs` module. The `fs` module provides functions for working with files.
const fs = require('fs');

// Get the name of the file to read from the command line arguments.
const file = process.argv[2];

// Read the file and store the contents in the `data` variable.
fs.readFile(file, 'utf8', (err, data) => {
  // Check if there was an error reading the file.
  if (err) {
    // If there was an error, log it to the console.
    console.log(err);
  } else {
    // If there was no error, log the contents of the file to the console.
    console.log(data);
  }
});
