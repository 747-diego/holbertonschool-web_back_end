import redis from 'redis';
const client = redis.createClient();

client.on('connect', function() {
 console.log('Redis client connected to the server');
});

client.on('error', function(connectionOff) {
  console.error(`Redis client not connected to the server: ${connectionOff.message}`);
});

function setNewSchool(schoolName, value) {  
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  const redisConfirmation = client.get(schoolName, redis.print);
  console.log(redisConfirmation);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
