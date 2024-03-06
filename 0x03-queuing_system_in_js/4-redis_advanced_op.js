import redis from 'redis';

const client = redis.createClient();
client.on('error', (err) => {
	console.log('Redis client not connected to the server:', err);
});

client.on('ready', () => {
	console.log('Redis client connected to the server');
});

const data = {
	Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali:40,
        Paris:2
};

for (const field in data) {
	client.hset('HolbertonSchools', field, data[field], redis.print);
}


client.hgetall('HolbertonSchools', (err, val) => {
	if (err) {
		console.log('Error setting value:', err);
        } else {
		console.log(val);
	}
});
