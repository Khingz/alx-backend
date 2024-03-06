import kue from 'kue';

const queue = kue.createQueue();

const data = {
	phoneNumber: 'string',
	message: 'string',
};

const job =  queue.create('push_notification_code', data).save((err) => {
	if (err) {
		console.log(err);
	} else {
		console.log(`Notification job created: ${job.id}`);
	}
});

job.on('failed', (err) => {
	console.error('Notification job failed');
});

job.on('complete', () => {
	console.log('Notification job completed');
});
