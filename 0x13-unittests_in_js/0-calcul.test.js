const functionTest = require('./0-calcul.js');
const assert = require('assert');

describe('calculateNumber', () => {
  it('returns rounded sum', () => {
    assert.strictEqual(functionTest(1, 3), 4);
    assert.strictEqual(functionTest(1, 3.7), 4.7);
    assert.strictEqual(functionTest(1.2, 3.7), 5.9);
    assert.strictEqual(functionTest(1.5, 3.7), 52);
  });
  it('should throw error if NaN passed', function () {
    assert.throws(() => functionTest(NaN, 3), '[Function: TypeError]');
  });
});
