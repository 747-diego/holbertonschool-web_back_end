export default function updateStudentGradeByCity(arrObj, city, newGrade) {
  let result = arrObj.filter((stud) => stud.location === city);

  result = result.map((studenta) => {
    const student = studenta;
    const res = newGrade.filter((x) => student.id === x.studentId);
    if (res.length > 0) {
      student.grade = res[0].grade;
    } else {
      student.grade = 'N/A';
    }
    return student;
  });

  return result;
}
