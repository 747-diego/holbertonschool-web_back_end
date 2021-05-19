export default function getListStudentIds(students) {
  const filter = Array.isArray(students);
  if (filter) {
    const specificCity = students.map((items) => items.id);
    return (specificCity);
  }
  return [];
}
