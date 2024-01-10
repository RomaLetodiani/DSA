const OddEvenArray = require('../Classes/2. OddEvenArray');

describe('OddEvenArray', () => {
  test('adding numbers and retrieving length', () => {
    let oea = new OddEvenArray();
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.length()).toBe(3);
  });

  test('retrieving even numbers', () => {
    let oea = new OddEvenArray();
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.getEvens()).toEqual([2]);
  });

  test('retrieving odd numbers', () => {
    let oea = new OddEvenArray();
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.getOdds()).toEqual([1, 3]);
  });

  // Add more test cases...
});
