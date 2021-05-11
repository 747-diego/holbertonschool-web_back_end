import { uploadPhoto, createUser } from './utils';

// export default function handleProfileSignup() {
//   let firstName;
//   let lastName;
//   let body;

//   return uploadPhoto()
//     .then((data) => {
//       body = data.body;
//       createUser()
//         .then((data) => {
//           firstName = data.firstName;
//           lastName = data.lastName;
//           console.log(`${body} ${firstName} ${lastName}`);
//         })
//         .catch(() => console.log('Signup system offline'));
//     })
//     .catch(() => console.log('Signup system offline'));
// }

export default function handleProfileSignup() {
  const x = uploadPhoto();
  const y = createUser();
  let firstName;
  let lastName;
  let body;

  return Promise.all([x, y])
    .then((values) => {
      body = values[0].body;
      firstName = values[1].firstName;
      lastName = values[1].lastName;
      console.log(`${body} ${firstName} ${lastName}`).catch(
        () => console.log('Signup system offline'));
    });
}
