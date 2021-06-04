import redis from 'redis';

const message = redis.createClient();
const user = redis.createClient();
const HolbieChannel = 'holberton school channel';

message.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

message.on('ready', () => {
  console.log('Redis client connected to the server');
});

user.subscribe(HolbieChannel);
user.on('message', (HolbieChannel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    user.unsubscribe();
    user.quit();
  }
});
