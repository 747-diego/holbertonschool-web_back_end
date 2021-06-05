import kue from 'kue';

const queue = kue.createQueue();
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const number = job.data.phoneNumber;
  const message = job.data.message;
  sendNotification(number, message);
});
