const functionTest = require("./0-calcul.js");
const mocha = require('mocha');
const assert = require("assert");

describe('calculateNumber', () => {
    it('returns rounded sum', () => {
    assert.strictEqual(functionTest(1, 3), 4);
    assert.strictEqual(functionTest(1.6, 3), 5);
    assert.strictEqual(functionTest(1.2, 3.8), 5);
    assert.strictEqual(functionTest(-1, -3), -4);
    assert.strictEqual(functionTest(-1.4, -3.6), -5);
    });
    it('should throw error if NaN passed', function () {
        assert.throws(() => functionTest(NaN, 3), '[Function: TypeError]');
    });
});