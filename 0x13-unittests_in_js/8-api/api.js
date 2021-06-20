const express = require('express');

const app = express();
const port = 7865;
const welcomeMessage = 'Welcome to the payment system';

app.get('/', (req, res) => {
  res.send(welcomeMessage);
});

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
