import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  const user = createUser();
  Promise.all([photo, user])
    .then((output) => console.log(output[0].body, output[1].firstName, output[1].lastName)).catch(() => console.log('Signup system offline'));
}
