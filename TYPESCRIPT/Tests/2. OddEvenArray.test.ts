import OddEvenArray from '../Classes/2. OddEvenArray';
describe('OddEvenArray', (): void => {
  let oea: OddEvenArray;

  beforeEach(() => {
    oea = new OddEvenArray();
  });

  test('adding numbers and getting the length', () => {
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.length()).toBe(3);
  });

  test('retrieving even numbers', () => {
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.getEvens()).toEqual([2]);
  });

  test('retrieving odd numbers', () => {
    oea.add(1);
    oea.add(2);
    oea.add(3);
    expect(oea.getOdds()).toEqual([1, 3]);
  });

  // Add more test cases as needed...
});
