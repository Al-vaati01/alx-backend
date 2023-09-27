#!/usr/bin/node
const redis = require('redis');

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage('Hello, Holberton!', 1000);

// Listen for messages on the subscribed channel
client.on('message', (_, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit if the message is 'KILL_SERVER'
    client.unsubscribe();
    client.quit();
  }
});
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
