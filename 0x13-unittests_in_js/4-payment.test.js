const { expect, assert } = require('chai');
const sinon = require('sinon');
const { spy } = require('sinon');

const sendPaymentRequestToApi = require('./4-payment');
const utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
  it('should call Util using spy and stub', () => {
    const spy = sinon.spy(utils, 'calculateNumber');
    // spy.returns(10);
    const log = sinon.spy(console, 'log');
    const api = sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.equal(true);
    expect(log.calledWithExactly('The total is: 10'));
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(api);

    spy.restore();
    log.restore();
  });
});
