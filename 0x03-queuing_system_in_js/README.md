# 0x03. Queuing System in JS

## Back-end
- JavaScript
- ES6
- Redis
- NodeJS
- ExpressJS
- Kue

## Resources
Read or watch:
- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis Client Interface](https://github.com/NodeRedis/node-redis)
- [Redis Client for Node JS](https://www.npmjs.com/package/redis)
- [Kue Deprecated but Still Used in the Industry](https://github.com/Automattic/kue)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Project Structure

### 0. Install a Redis Instance (mandatory)
- Download, extract, and compile the latest stable Redis version (higher than 5.0.7) from [Redis Downloads](https://redis.io/download/):

```bash
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
