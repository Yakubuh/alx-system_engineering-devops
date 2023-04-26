#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const arg_ = argv[2];
const url = arg_;
request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  const dict = {};
  const json_ = JSON.parse(body);
  for (const property of json_) {
    if (!(property.userId in dict)) {
      dict[property.userId] = 0;
    }
    if (property.completed === true) {
      dict[property.userId] += 1;
    }
  }
  console.log(dict);
});
