import HashArray from '../Classes/5. HashArray';
describe('HashArray', () => {
  let ha: HashArray;

  beforeEach(() => {
    ha = new HashArray();
  });

  test('isEmpty', () => {
    expect(ha.isEmpty()).toBe(true);
    ha.push('roma');
    expect(ha.isEmpty()).toBe(false);
  });

  test('includes', () => {
    ha.push('roma');
    ha.push('paris');
    ha.push('london');
    expect(ha.includes('roma')).toBe(true);
    expect(ha.includes('tokyo')).toBe(false);
  });

  test('push and get Length', () => {
    expect(ha.getLength()).toBe(0);
    ha.push('roma');
    ha.push('paris');
    expect(ha.getLength()).toBe(2);
  });

  test('remove', () => {
    ha.push('roma');
    ha.push('paris');
    ha.push('london');
    ha.remove('paris');
    expect(ha.getLength()).toBe(2);
    expect(ha.includes('paris')).toBe(false);
  });

  // Add more test cases as needed...
});
