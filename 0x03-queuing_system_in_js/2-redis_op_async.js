import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.on('error', (err) => {
	console.log('Redis client not connected to the server:', err);
});

client.on('ready', () => {
	console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async (schoolName) => {
	console.log(await promisify(client.GET).bind(client)(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
