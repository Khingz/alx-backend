import { createClient, print } from 'redis';

const client = createClient();
client.on('error', (err) => {
	console.log('Redis client not connected to the server:', err);
});

client.on('ready', () => {
	console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error('Error setting value:', err);
        } else {
            console.log('Reply:', reply);
        }
    });
};

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error('Error getting value:', err);
        } else {
            console.log(reply);
        }
    });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
