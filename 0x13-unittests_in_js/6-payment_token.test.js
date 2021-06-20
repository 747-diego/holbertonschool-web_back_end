const { expect } = require('chai');
// const sinon = require('sinon');

const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('promise response from API should resolve', () => {
    const test = getPaymentTokenFromAPI(true);
    const response = await test;
    expect(response).to.eql({ data: 'Successful response from the API' });
    console.log(response);
  });
});
