import kue from 'kue';
export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw (Error('Jobs is not an array'));
  }

  jobs.forEach((job) => {
    const eachJob = queue.create('push_notification_code_3', job).save(
      (error) => {
        if (!error) {
          console.log(`Notification job created: ${eachJob.id}`);
        }
      });
    eachJob.on('complete', () => {
      console.log(`Notification job ${eachJob.id} completed`)
    });
    eachJob.on('failed', (err) => {
      console.log(`Notification job ${eachJob.id} failed: ${err}`)
    });
    eachJob.on('progress', (progress) => {
      console.log(`Notification job ${eachJob.id} ${progress}% complete`)
    });
  });
}
