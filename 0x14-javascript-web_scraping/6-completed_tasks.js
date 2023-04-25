#!/usr/bin/node

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// Make an HTTP GET request to the URL specified by the first command-line argument.
request(process.argv[2], (err, response, body) => {
  // Check if there was an error.
  if (err) {
    // If there was an error, log it to the console and exit.
    console.error(err);
    return;
  }

  // Parse the JSON response body.
  const json = JSON.parse(body);

  // Initialize an empty object to store the completed tasks for each user.
  const resp = {};

  // Iterate over the JSON array.
  for (let i = 0; i < json.length; i++) {
    // Check if the current task is completed.
    if (json[i].completed === true) {
      // If the current task is completed, check if the user ID exists in the `resp` object.
      if (resp[json[i].userId] === undefined) {
        // If the user ID does not exist in the `resp` object, initialize the count to 0.
        resp[json[i].userId] = 0;
      }

      // Increment the count for the current user.
      resp[json[i].userId]++;
    }
  }

  // Log the `resp` object.
  console.log(resp);
});
