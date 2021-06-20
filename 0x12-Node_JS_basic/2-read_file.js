const data = require('fs');

function countStudents (file) {
  const classroom = {};
  let seats = 0;
  let name;

  try {
    name = data.readFileSync(file, { encoding: 'utf8', flag: 'r' });
  } catch (error) {
    throw (new Error('Cannot load the database'));
  }
  const names = name.split('\n');
  const students = names.slice(1).map((student) => student.split(',')).filter((student) => student.length > 0 && student[0] !== '');
  for (const student of students) {
    seats += 1;
    if (!(student[3] in classroom)) {
      classroom[student[3]] = [];
    }
    classroom[student[3]].push(student[0]);
  }
  console.log(`Number of students: ${seats}`);
  for (const num of Object.keys(classroom)) {
    console.log(`Number of students in ${num}: ${classroom[num].length}. List: ${classroom[num].join(', ')}`);
  }
}
module.exports = countStudents;
