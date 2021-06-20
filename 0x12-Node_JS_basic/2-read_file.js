const fs = require('fs');

function countStudents(path) {
  const student = {};
  let len = 0;
  let data;

  try {
    data = fs.readFileSync(path, { encoding: 'utf8', flag: 'r' });
  } catch (err) {
    throw new Error('Cannot load the database');
  }

  const datalines = data.split('\n');
  const students = datalines.slice(1).map((line) => line.split(',')).filter((line) => line.length > 0 && line[0] !== '');

  for (const line of students) {
    len += 1;
    if (!(line[3] in student)) {
      student[line[3]] = [];
    }
    student[line[3]].push(line[0]);
  }

  console.log(`Number of students: ${len}`);
  for (const i of Object.keys(student)) {
    console.log(`Number of students in ${i}: ${student[i].length}. List: ${student[i].join(', ')}`);
  }
}
module.exports = countStudents;
