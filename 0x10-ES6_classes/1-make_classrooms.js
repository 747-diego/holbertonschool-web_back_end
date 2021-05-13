import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const classArray = [];
  //   const students = [19, 20, 34];
  const classroomOne = [19];
  const classroomTwo = [20];
  const classroomThree = [34];
  const roomOne = classArray.push(new ClassRoom(classroomOne));
  const roomTwo = classArray.push(new ClassRoom(classroomTwo));
  const roomThree = classArray.push(new ClassRoom(classroomThree));

  return ([roomOne, roomTwo, roomThree]);
}
