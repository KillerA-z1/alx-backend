import kue from 'kue';

const queue = kue.createQueue();
const blacklistedPhones = ['4153518780', '4153518781'];

/**
 * Function to send notification
 * @param {string} phoneNumber - The phone number to send the notification to
 * @param {string} message - The message to send
 * @param {object} job - The job object
 * @param {function} done - The callback to execute when done
 */
function sendNotification(phoneNumber, message, job, done) {
  // Track progress: 0 out of 100
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedPhones.includes(phoneNumber)) {
    // Fail the job with an error
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed(error.message, error);
    done(error);
    return;
  }

  // Track progress: 50 out of 100
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Simulate some asynchronous operation (e.g., sending an actual notification)
  setTimeout(() => {
    // Assume the notification was sent successfully
    job.progress(100, 100);
    done();
  }, 1000);
}

// Process jobs from the 'push_notification_code_2' queue with concurrency 2
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Optional: Handle global queue errors
queue.on('error', (err) => {
  console.error('Queue Error:', err);
});