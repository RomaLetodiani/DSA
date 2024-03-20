import MyObject from '../Classes/6. myObject';
describe('MyObject', () => {
  let myObject: MyObject;

  beforeEach(() => {
    myObject = new MyObject();
  });

  test('set and get', () => {
    myObject.set('name', 'John');
    expect(myObject.get('name')).toBe('John');
  });

  test('update existing key-value pair', () => {
    myObject.set('name', 'John');
    myObject.set('name', 'Jane');
    expect(myObject.get('name')).toBe('Jane');
  });

  test('return undefined for non-existing key', () => {
    expect(myObject.get('nonexistent')).toBe(undefined);
  });

  test('includes', () => {
    myObject.set('name', 'John');
    expect(myObject.includes('name')).toBe(true);
    expect(myObject.includes('nonexistent')).toBe(false);
  });

  test('remove', () => {
    myObject.set('name', 'John');
    myObject.remove('name');
    expect(myObject.includes('name')).toBe(false);
    expect(myObject.getLength()).toBe(0);
  });

  test('resizing buckets', () => {
    for (let i = 0; i < 10; i++) {
      myObject.set(`key${i}`, `value${i}`);
    }
    expect(myObject.getLength()).toBe(10);
    // The number of buckets may vary depending on implementation details,
    // so we just check that it's greater than the initial length
    expect(myObject.buckets.length).toBeGreaterThan(4);
  });

  // Add more test cases as needed...
});
