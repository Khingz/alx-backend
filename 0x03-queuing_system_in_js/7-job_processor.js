import kue from 'kue';

const queue = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
	job.progress(0, 100);
	if (blacklist.includes(phoneNumber)) {
		done(Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}
	job.progress(50, 100);
	console.log(
		`Sending notification to ${phoneNumber}, with message: ${message}`
	);
 	done();
}

queue.process('push_notification_code_2', (job, done) => {
        const num = job.data.phoneNumber;
        const msg = job.data.message;
        sendNotification(num, msg, job, done);
});
