import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const cueTest = kue.createQueue();
before(function() {
  cueTest.testMode.enter();
});
