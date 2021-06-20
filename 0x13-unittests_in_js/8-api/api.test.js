const request = require('request');
const chai = require('chai');
const { expect } = require('chai');

describe('API test', () => {
  it('respond with 200 code and body', (done) => {
    request('http://localhost:7865', 'GET', (error, response, message) => {
      if (error) {
        throw (error);
      }
      expect(response.statusCode).to.equal(200);
      expect(message).to.equal('Welcome to the payment system');
    });
    done();
  });
});
