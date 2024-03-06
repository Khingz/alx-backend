const createPushNotificationsJobs = (jobs, queue) => {
	if (!Array.isArray(jobs)) {
		throw new Error('Jobs is not an array');
	}
	jobs.forEach((item) => {
		const job =  queue.create('push_notification_code_3', item).save((err) => {
			if (!err) {
                        	console.log(`Notification job created: ${job.id}`);
			}
		});
		job.on('failed', (err) => {
			console.log(`Notification job ${job.id} failed:`, err);
        	});
		job.on('complete', () => {
			console.log(`Notification job ${job.id} completed`);
		});
		job.on('progress', (progress, data) => {
			console.log(`Notification job ${job.id} ${progress}% complete`);
		});
	});
}

export default createPushNotificationsJobs;
