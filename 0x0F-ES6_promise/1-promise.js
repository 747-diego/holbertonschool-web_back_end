export default function getFullResponseFromAPIj(success) {
  const APIresponse = new Promise((resolve, reject) => {
    if (success) {
      resolve(
        { status: 200, body: 'Success' },
      );
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
  return (APIresponse);
}
