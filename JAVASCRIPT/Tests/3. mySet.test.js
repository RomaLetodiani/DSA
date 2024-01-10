const MySet = require('../Classes/3. mySet.js');

describe('MySet', () => {
  let mySet;
  beforeEach(() => {
    mySet = new MySet();
    mySet.add('hello');
    mySet.add('world');
    mySet.add('how');
    mySet.add('are');
    mySet.add('you');
  });
  test('adding and retrieving values', () => {
    expect(mySet.values()).toEqual(['world', 'are', 'you', 'hello', 'how']);
  });

  test('removing values', () => {
    mySet.delete('world');
    expect(mySet.values()).toEqual(['are', 'you', 'hello', 'how']);
  });

  test('clearing values', () => {
    mySet.clear();
    expect(mySet.values()).toEqual([]);
  });

  test('checking for values', () => {
    expect(mySet.has('world')).toBe(true);
    expect(mySet.has('hello')).toBe(true);
    expect(mySet.has('how')).toBe(true);
    expect(mySet.has('are')).toBe(true);
    expect(mySet.has('you')).toBe(true);
    expect(mySet.has('helloo')).toBe(false);
    expect(mySet.has('heloo')).toBe(false);
  });

  test('getting values', () => {
    expect(mySet.get('world')).toBe('world');
    expect(mySet.get('hello')).toBe('hello');
    expect(mySet.get('how')).toBe('how');
    expect(mySet.get('are')).toBe('are');
    expect(mySet.get('you')).toBe('you');
    expect(mySet.get('helloo')).toBe(undefined);
    expect(mySet.get('heloo')).toBe(undefined);
  });

  // Add more test cases...
});
