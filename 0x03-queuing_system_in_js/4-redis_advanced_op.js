#!/usr/bin/node
const redis = require('redis');

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hsetKey = 'HolbertonSchools';
const obj = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
};

for (const key in obj) {
  const val = obj[key];
  client.hset(hsetKey, key, val, redis.print);
}

client.hgetall(hsetKey, (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Hash stored in Redis:');
    console.log(result);
  }
});

client.quit();
