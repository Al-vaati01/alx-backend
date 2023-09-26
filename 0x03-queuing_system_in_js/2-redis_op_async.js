#!/usr/bin/node
const redis = require('redis');
const util = require('util');

const client = redis.createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`${schoolName} was not set: ${err}`);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
};

const getValueCallback = (schoolName, callback) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      callback(err, null);
    } else {
      callback(null, value);
    }
  });
};

const getValue = util.promisify(getValueCallback);

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getValue(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
