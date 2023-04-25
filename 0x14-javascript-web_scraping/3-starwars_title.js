#!/usr/bin/node

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// The URL to request.
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

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

  // Log the title of the film.
  console.log(data.title);
});

