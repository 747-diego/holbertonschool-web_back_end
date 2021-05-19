export default function updateStudentGradeByCity(students, city, newGrades) {
  const getListStudents = students.filter((student) => student.location === city);
  return getListStudents.map((student) => {
    return ({
      ...student,
      grade: newGrades.filter((specificCity) => specificCity.studentId === student.id) ? newGrades.filter((specificCity) => specificCity.studentId === student.id).grade : 'N/A'
    });
  });
}
