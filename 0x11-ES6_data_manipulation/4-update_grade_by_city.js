export default function updateStudentGradeByCity(arrObj, city, newGrade) {
  let response = arrObj.filter((stud) => stud.location === city);

  response = response.map((students) => {
    // const students = students;
    const score = newGrade.filter((city) => students.id === city.studentId);
    if (score.length > 0) {
      students.grade = score[0].grade;
    } else {
      students.grade = 'N/A';
    }
    return (students);
  });

  return (response);
}
