#!/usr/bin/node

// Import the `fs` module. The `fs` module provides functions for working with files.
const fs = require('fs');

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// Get the URL from the command line arguments.
const url = process.argv[2];

// Get the file path from the command line arguments.
const filePath = process.argv[3];

// Make an HTTP GET request to the URL.
request(url, (err, res, body) => {
  // Check if there was an error.
  if (err) {
    // If there was an error, log it to the console and exit.
    console.log(err);
    return;
  }

  // Write the body of the response to the file in the UTF-8 encoding.
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    // Check if there was an error.
    if (err) {
      // If there was an error, log it to the console and exit.
      console.log(err);
      return;
    }

    // The file has been written successfully.
    console.log(`File ${filePath} has been written successfully.`);
  });
});
