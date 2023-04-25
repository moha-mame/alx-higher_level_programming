#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, { json: true }, (err, res, body) => {
  if (err) { return console.error(err); }
  const completedTasksByUser = body.reduce((acc, curr) => {
    if (curr.completed) {
      acc[curr.userId] = (acc[curr.userId] || 0) + 1;
    }
    return acc;
  }, {});
  for (const userId in completedTasksByUser) {
    console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks`);
  }
});
