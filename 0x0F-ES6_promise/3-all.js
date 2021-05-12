import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then((profileSetup) => {
    console.log(profileSetup[0].body, profileSetup[1].firstName, profileSetup[1].lastName);
  }, () => console.log('Signup system offline'));
}
