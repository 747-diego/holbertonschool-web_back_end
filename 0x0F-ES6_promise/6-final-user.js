import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = await signUpUser(firstName, lastName).then((valueOrError) => ({
    status: 'status_of_the_promise',
    value: valueOrError,
  }));

  const userData = await uploadPhoto(fileName).catch((valueOrError) => ({
    status: 'value or error returned by the Promise',
    value: valueOrError.toString(),
  }));

  const promiseArray = Promise.resolve([userPromise, userData]);
  return (promiseArray);
}
