export default function signUpUser(firstName, lastName) {
  const user = new Promise((resolve) => {
    resolve(
      { firstName, lastName },
    );
  });
  return (user);
}
