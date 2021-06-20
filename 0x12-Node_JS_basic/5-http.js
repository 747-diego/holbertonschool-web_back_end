const fs = require('fs');
const util = require('util');
const http = require('http');

const readFile = util.promisify(fs.readFile);

function countStudents(file) {
  return readFile(file, 'utf8').then((data) => {
    const classroom = {};
    let seats = 0;

    const sep = data.split('\n');
    const students = sep.slice(1).map((seat) => seat.split(',')).filter((seat) => seat.length > 0 && seat[0] !== '');

    for (const student of students) {
      seats += 1;
      if (!(student[3] in classroom)) {
        classroom[student[3]] = [];
      }
      classroom[student[3]].push(student[0]);
    }

    console.log(`Number of students: ${seats}`);
    for (const i of Object.keys(classroom)) {
      console.log(`Number of students in ${i}: ${classroom[i].length}. List: ${classroom[i].join(', ')}`);
    }
  }).catch(() => {
    throw new Error('Cannot load the database');
  });
}

const app = http.createServer(async (req, res) => {
  let students;
  res.writeHead(200, 'Content-Type', 'text/plain');
  switch (req.url) {
    case '/students':
      students = await countStudents(process.argv[2]);
      res.write(`This is the list of our students\n${students}`);
      res.end();
      break;

    default:
      res.write('Hello Holberton School!');
      res.end();
      break;
  }
}).listen(1245);

module.exports = app;
