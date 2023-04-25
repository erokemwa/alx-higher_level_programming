#!/usr/bin/node

// Import the `fs` module. The `fs` module provides functions for working with files.
const fs = require('fs');

// Get the name of the file to write to from the command line arguments.
const file = process.argv[2];

// Get the input to write to the file from the command line arguments.
const input = process.argv[3];

// Write the input to the file.
fs.writeFile(file, input, (err) => {
  // Check if there was an error writing to the file.
  if (err) {
    // If there was an error, log it to the console.
    console.log(err);
  }
});

