import redis from 'redis';

const client = redis.createClient();
client.on('error', (err) => {
	console.log('Redis client not connected to the server:', err);
});

client.on('ready', () => {
	console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
	if (message === 'KILL_SERVER') {
		console.log(message);
		client.unsubscribe(channel);
	} else {
		console.log(message);
	}
});
