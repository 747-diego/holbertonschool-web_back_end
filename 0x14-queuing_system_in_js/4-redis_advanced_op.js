import redis from 'redis';

const client = redis.createClient();

async function displayValues(values) {
  for (const key in values) {
    client.hset('HolbertonSchools', key, values[key], redis.print);
  }

  const storedObject = client.hgetall('HolbertonSchools');
  console.log(storedObject);
}

const cities = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

displayValues(cities);
