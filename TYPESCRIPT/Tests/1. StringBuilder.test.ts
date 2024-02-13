import StringBuilder from '../Classes/1. StringBuilder';
describe('StringBuilder', (): void => {
  let sb: StringBuilder;

  beforeEach((): void => {
    sb = new StringBuilder('Hello');
  });

  test('append, get length', () => {
    sb.append(', ');
    sb.append('World!');
    expect(sb.get_length()).toBe(13);
  });

  test('get string', () => {
    sb.append(', ');
    sb.append('World!');
    expect(sb.get_string()).toBe('Hello, World!');
  });

  test('append empty string', () => {
    sb.append('');
    expect(sb.get_string()).toBe('Hello');
  });

  test('append a very large string and measure efficiency', () => {
    const longString: string = 'a'.repeat(100000); // Creating a large string
    const start: number = performance.now(); // Start time measurement
    for (let i = 0; i < 100000; i++) {
      sb.append(longString[i]);
    }
    const end: number = performance.now(); // End time measurement
    expect(sb.get_length()).toBe(100005);
    expect(end - start).toBeLessThanOrEqual(10);
  });
});
