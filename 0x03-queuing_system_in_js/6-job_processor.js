import kue from 'kue';

const queue = kue.createQueue();

const sendNotification = (phoneNumber, message) => {
	console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
	const num = job.data.phoneNumber;
	const msg = job.data.message;
	sendNotification(num, msg);
	done();
});
