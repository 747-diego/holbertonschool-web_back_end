const http = require('http');

const welcome = 'Hello Holberton School!';
const port = 1245;

const app = http.createServer((req, res) => {
  res.end(welcome);
});

app.listen(port, '127.0.0.1');

module.exports = app;
