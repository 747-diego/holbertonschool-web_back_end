import redis from 'redis';
const client = redis.createClient();
const {req} = require('util');

function reserveSeat(number) {
  client.set('available_seats', number);
}
