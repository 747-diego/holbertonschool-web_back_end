const express = require('express');

const app = express();
const welcome = 'Hello Holberton School!';

app.get('/', (req, res) => {
  res.send(welcome);
}).listen(1245);

module.exports = app;
