#!/usr/bin/node

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// The URL to request.
const url = process.argv[2];

// Make an HTTP GET request to the URL.
request(url, (err, res, body) => {
  // Check if there was an error.
  if (err) {
    // If there was an error, log it to the console.
    console.error(err);
    return;
  }

  // Parse the JSON response body.
  const data = JSON.parse(body);

  // Initialize a counter to keep track of the number of characters who are 18 years old or older.
  let count = 0;

  // Iterate over the results array.
  for (let i = 0; i < data.results.length; i++) {
    // Get the characters array for the current result.
    const chars = data.results[i].characters;

    // Iterate over the characters array.
    for (let k = 0; k < chars.length; k++) {
      // Check if the current character's name includes the string "18".
      if (chars[k].includes('18')) {
        // If the current character's name includes the string "18", increment the counter.
        count++;
      }
    }
  }

  // Log the number of characters who are 18 years old or older.
  console.log(count);
});
