#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  } else {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Saved response body to ${filePath}`);
      }
    });
  }
});
