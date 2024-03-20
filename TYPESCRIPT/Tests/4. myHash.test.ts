import myHash from '../Classes/4. myHash';
describe('myHash', () => {
  it('should produce different hash values for different strings', () => {
    const string1 = 'hello';
    const string2 = 'world';
    const hash1 = myHash(string1);
    const hash2 = myHash(string2);
    expect(hash1).not.toBe(hash2);
  });

  it('should exhibit low collision probability for a large set of random strings', () => {
    const numStrings = 100000;
    const hashes = new Map();
    for (let i = 0; i < numStrings; i++) {
      const randomString = Math.random().toString(36).substring(2);
      const hash = myHash(randomString);

      // If a collision is found, log a warning message but continue testing
      if (hashes.has(hash)) {
        console.warn(
          `Collision detected on attempt ${i + 1} for strings: ${hashes.get(hash)}, ${randomString}. hash: ${hash}`
        );
      } else {
        hashes.set(hash, randomString);
      }
    }

    // Check for a reasonable number of unique hashes
    expect(hashes.size).toBeGreaterThan(numStrings * 0.95); // Expect at least 95% unique hashes
  });

  it('should return the same hash value for the same string input', () => {
    const string = 'hello world';
    const hash1 = myHash(string);
    const hash2 = myHash(string);
    expect(hash1).toBe(hash2);
  });

  it('should return a positive integer for any string input', () => {
    const string = 'test string';
    const hash = myHash(string);
    expect(hash).toBeGreaterThan(0);
    expect(Number.isInteger(hash)).toBe(true);
  });
});
