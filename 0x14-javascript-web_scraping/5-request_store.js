#!/usr/bin/node

const request = require('request');
const fs = require('fs/promises');

const [url, filePath] = process.argv.slice(2);

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8')
      .then(() => {
        console.log(`Successfully saved the contents of ${url} to ${filePath}`);
      })
      .catch((error) => {
        console.error(`Error writing file: ${error}`);
      });
  } else {
    console.error(`Request failed with status code: ${response.statusCode}`);
  }
});
