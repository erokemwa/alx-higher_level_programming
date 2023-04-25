#!/usr/bin/node

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// Get the URL to request from the command line arguments.
const url = process.argv[2];

// Make an HTTP GET request to the URL.
request.get(url).on('response', (response) => {
  // Check the status code of the response.
  console.log(`code: ${response.statusCode}`);
});
