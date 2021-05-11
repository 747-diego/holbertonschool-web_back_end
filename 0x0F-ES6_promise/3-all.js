import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const x = uploadPhoto();
  const y = createUser();
  let body;
  let firstName;
  let lastName;
  return Promise.all([x, y]).then((values) => {
    firstName = values.firstName;
    lastName = values.lastName;
    body = values.body;
    console.log(firstName, lastName, body);
  }, () => console.log('Signup system offline'));
}
