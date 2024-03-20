import MySet from '../Classes/3. mySet';

describe('MySet', () => {
  let mySet: MySet;

  beforeEach(() => {
    mySet = new MySet();
  });

  test('add and size', () => {
    mySet.add('hello');
    mySet.add('world');
    mySet.add('how');
    expect(mySet.size()).toBe(3);
  });

  test('values', () => {
    mySet.add('hello');
    mySet.add('world');
    mySet.add('how');
    expect(mySet.values()).toEqual(['world', 'hello', 'how']);
  });

  test('has', () => {
    mySet.add('hello');
    mySet.add('world');
    expect(mySet.has('world')).toBe(true);
    expect(mySet.has('how')).toBe(false);
  });

  test('get', () => {
    mySet.add('hello');
    mySet.add('world');
    expect(mySet.get('hello')).toBe('hello');
    expect(mySet.get('how')).toBe(undefined);
  });

  test('delete', () => {
    mySet.add('hello');
    mySet.add('world');
    mySet.delete('world');
    expect(mySet.has('world')).toBe(false);
    expect(mySet.size()).toBe(1);
  });

  test('clear', () => {
    mySet.add('hello');
    mySet.add('world');
    mySet.clear();
    expect(mySet.size()).toBe(0);
  });

  // Add more test cases as needed...
});
