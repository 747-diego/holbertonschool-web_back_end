const express = require('express')
const app = express()
const port = 7865;
const welcomeMessage = 'Welcome to the payment system';
const APIconnected = 'API available on localhost port 7865';

app.get('/', function(req, res) {
  res.send(welcomeMessage);
});

app.listen(port, function() {
  console.log(APIconnected);
});
