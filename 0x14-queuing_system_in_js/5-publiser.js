import redis from 'redis';

const user = redis.createClient();

user.on('connected', () {
  console.log('Redis client connected to the server');
});

user.on('error', (error) {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    user.publish('holberton school channel', message);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);