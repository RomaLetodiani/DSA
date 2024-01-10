const OddEvenArray = require('../Classes/2. OddEvenArray');

describe('OddEvenArray', () => {
  // Initialize an OddEvenArray object
  let oea;

  beforeEach(() => {
    oea = new OddEvenArray('Hello');
    oea.add(1);
    oea.add(2);
    oea.add(3);
  });

  test('adding numbers and retrieving length', () => {
    expect(oea.length()).toBe(3);
  });

  test('retrieving even numbers', () => {
    expect(oea.getEvens()).toEqual([2]);
  });

  test('retrieving odd numbers', () => {
    expect(oea.getOdds()).toEqual([1, 3]);
  });

  // Add more test cases...
});
