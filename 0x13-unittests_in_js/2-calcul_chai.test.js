const functionTest = require('./2-calcul.js');
const { expect } = require('chai');

describe('calculateNumber', () => {
  it('ADDITION IS COMPLETE', () => {
    expect(functionTest('SUM', 1, 3).to.equal(4));
    expect(functionTest('SUM', 1, 3.7).to.equal(5));
    expect(functionTest('SUM', 1.2, 3.7).to.equal(5));
    expect(functionTest('SUM', 1.5, 3.7).to.equal(6));
    expect(functionTest('SUM', 1.4, 4.5).to.equal(6));
    expect(functionTest('SUM', 1.4, 0).to.equal(1));
    expect(functionTest('SUM', 0, 1.4).to.equal(1));
  });
});

describe('calculateNumber', () => {
  it('SUBTRACTION IS COMPLETE', () => {
    expect(functionTest('SUBTRACT', 1, 3).to.equal(-2));
    expect(functionTest('SUBTRACT', 1, 3.7).to.equal(-3));
    expect(functionTest('SUBTRACT', 1.2, 3.7).to.equal(-3));
    expect(functionTest('SUBTRACT', 1.5, 3.7).to.equal(-2));
    expect(functionTest('SUBTRACT', 1.4, 4.5).to.equal(-4));
    expect(functionTest('SUBTRACT', 1.4, 0).to.equal(1));
    expect(functionTest('SUBTRACT', 0, 1.4).to.equal(-1));
  });
});

describe('calculateNumber', () => {
  it('DIVISION IS COMPLETE', () => {
    expect(functionTest('DIVIDE', 9, 3).to.equal(3));
    expect(functionTest('DIVIDE', 12, 3).to.equal(4));
    expect(functionTest('DIVIDE', 60, 5).to.equal(12));
    expect(functionTest('DIVIDE', 24, 3).to.equal(8));
    expect(functionTest('DIVIDE', 144, 12).to.equal(12));
    expect(functionTest('DIVIDE', 30, 5).to.equal(6));
    expect(functionTest('DIVIDE', 0, 1.4).to.equal(0));
    expect(functionTest('DIVIDE', 1.4, 0).to.equal('Error'));
  });
});
