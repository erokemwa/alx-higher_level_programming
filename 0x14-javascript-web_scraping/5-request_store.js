#!/usr/bin/node

// Import the `request` and `fs` modules. The `request` module provides functions for making HTTP requests. The `fs` module provides functions for working with files.
const request = require('request');
const fs = require('fs');

// The URL to request.
const url = process.argv[2];

// The file to write the response body to.
const filename = process.argv[3];

// Make an HTTP GET request to the URL.
request(url, function (err, res, body) {
  // Check if there was an error.
  if (err) {
    // If there was an error, log it to the console and exit.
    console.log(err);
    return;
  }

  // Write the response body to the file.
  fs.writeFile(filename, body, 'utf8', function (err) {
    if (err) {
      // If there was an error, log it to the console.
      console.log(err);
    }
  });
});
