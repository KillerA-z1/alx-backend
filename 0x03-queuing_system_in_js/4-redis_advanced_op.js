import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hashKey = 'HolbertonSchools';

client.hset(hashKey, 'Portland', 50, print);
client.hset(hashKey, 'Seattle', 80, print);
client.hset(hashKey, 'New York', 20, print);
client.hset(hashKey, 'Bogota', 20, print);
client.hset(hashKey, 'Cali', 40, print);
client.hset(hashKey, 'Paris', 2, print);

client.hgetall(hashKey, (err, result) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log(result);
  }
});
