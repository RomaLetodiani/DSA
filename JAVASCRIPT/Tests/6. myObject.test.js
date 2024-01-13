const MyObject = require('../Classes/6. myObject'); // Assuming your class is in a separate file

describe('MyObject', () => {
  let myObject;

  beforeEach(() => {
    myObject = new MyObject();
  });

  test('should add key-value pair and retrieve value', () => {
    myObject.set('name', 'John');
    expect(myObject.get('name')).toBe('John');
  });

  test('should update existing key-value pair', () => {
    myObject.set('name', 'John');
    myObject.set('name', 'Jane');
    expect(myObject.get('name')).toBe('Jane');
  });

  test('should return undefined for non-existing key', () => {
    expect(myObject.get('nonexistent')).toBeUndefined();
  });

  test('should check if key exists', () => {
    myObject.set('name', 'John');
    expect(myObject.includes('name')).toBe(true);
    expect(myObject.includes('nonexistent')).toBe(false);
  });

  test('should remove key-value pair', () => {
    myObject.set('name', 'John');
    myObject.remove('name');
    expect(myObject.includes('name')).toBe(false);
    expect(myObject.getLength()).toBe(0);
  });

  test('should resize buckets', () => {
    for (let i = 0; i < 10; i++) {
      myObject.set(`key${i}`, `value${i}`);
    }

    expect(myObject.getLength()).toBe(10);
    expect(myObject.buckets.length).toBeGreaterThan(4); // Assuming you have a minimum bucket size of 4

    // Add more specific assertions based on your expected behavior during resizing
  });
});
