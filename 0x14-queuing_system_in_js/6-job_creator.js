import kue from 'kue';

const job = kue.createQueue();
const contactInfo = {
  phoneNumber: '2038325152',
  message: 'contact number',
};

const jobListing = job.create('push_notification_code', contactInfo).save(
  (errorMessage) => {
    if (!errorMessage) console.log(`Notification job created: ${jobListing.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
