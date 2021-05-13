import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classArray = [];
  //   const students = [19, 20, 34];
  const classroomOne = [19];
  const classroomTwo = [20];
  const classroomThree = [34];
  classArray.push(new ClassRoom(classroomOne));
  classArray.push(new ClassRoom(classroomTwo));
  classArray.push(new ClassRoom(classroomThree));

  return (classArray);
}
