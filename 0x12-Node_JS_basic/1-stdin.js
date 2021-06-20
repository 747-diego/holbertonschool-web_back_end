process.stdin.setEncoding('utf8');
console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
  const userInputName = process.stdin.read();
  if (userInputName !== null) {
    process.stdout.write(`Your name is: ${userInputName}`);
  }
});

process.stdin.on('end', () => {
  if ((process.stdin.isTTY !== null)) {
    console.log('This important software is now closing');
  }
});
