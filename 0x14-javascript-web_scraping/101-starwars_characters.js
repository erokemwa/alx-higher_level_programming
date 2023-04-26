#!/usr/bin/node

// Import the `request` module. The `request` module provides functions for making HTTP requests.
const request = require('request');

// The URL to request.
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

// Make an HTTP GET request to the URL.
request(url, (err, res, body) => {
  // Check if there was an error.
  if (err) {
    // If there was an error, log it to the console and exit.
    console.log(err);
    return;
  }

  // Parse the JSON response body.
  const characters = JSON.parse(body).characters;

  // Create a function to print the characters.
  const printCharacter = (i) => {
    // Make an HTTP GET request to the character URL.
    request(characters[i], (err, res, body) => {
      // Check if there was an error.
      if (err) {
        // If there was an error, log it to the console and exit.
        console.log(err);
        return;
      }

      // Parse the JSON response body.
      const character = JSON.parse(body);

      // Log the character's name.
      console.log(character.name);

      // If there are more characters, call the `printCharacter` function again.
      if (i + 1 < characters.length) {
        printCharacter(i + 1);
      }
    });
  };

  // Print the first character.
  printCharacter(0);
});
