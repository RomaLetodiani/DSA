const StringBuilder = require('../Classes/1. StringBuilder');

describe('StringBuilder', () => {
  let sb;

  beforeEach(() => {
    sb = new StringBuilder('Hello');
  });
  test('appending strings and retrieving length', () => {
    sb.append(', ');
    sb.append('World!');
    expect(sb.get_length()).toBe(13);
  });

  test('retrieving the final string', () => {
    sb.append(', ');
    sb.append('World!');
    expect(sb.get_string()).toBe('Hello, World!');
  });

  // Add more test cases...

  test('appending a large string', () => {
    let longString = 'a'.repeat(100000);
    sb.append(longString);
    expect(sb.get_length()).toBe(100005);
  });
});
