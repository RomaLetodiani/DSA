const myHash = require('../Classes/4. myHash');

describe('myHash', () => {
  test('hash of empty string', () => {
    const hash = myHash('');
    expect(hash).toEqual(0);
  });

  test('hash of single character string', () => {
    const hash = myHash('a');
    expect(hash).not.toEqual(0);
  });

  test('hash of "hello"', () => {
    const hash = myHash('hello');
    expect(hash).toBeDefined();
    expect(typeof hash).toBe('number');
  });

  test('collision check for "hello" and "olleh"', () => {
    const hash = myHash('hello');
    const hash1 = myHash('olleh');
    expect(hash).not.toBe(hash1);
  });

  test('hash of a string with special characters', () => {
    const hashSpecial = myHash('!@#$%^&*()');
    expect(hashSpecial).toBeDefined();
    expect(typeof hashSpecial).toBe('number');
  });

  test('hash of different strings', () => {
    const hashHello = myHash('hello');
    const hashWorld = myHash('world');
    expect(hashHello).not.toEqual(hashWorld);
  });

  test('hash of repeated characters', () => {
    const hash1 = myHash('aaa');
    const hash2 = myHash('aaaa');
    expect(hash1).not.toEqual(hash2);
  });

  test('hash of a long string', () => {
    const longString = 'a'.repeat(1000);
    const hashLong = myHash(longString);
    expect(hashLong).toBeDefined();
    expect(typeof hashLong).toBe('number');
  });
});
