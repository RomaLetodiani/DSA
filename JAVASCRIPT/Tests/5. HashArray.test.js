const HashArray = require('../Classes/5. HashArray');

describe('testing HashArray', () => {
  let hashArray;
  beforeEach(() => {
    hashArray = new HashArray();
  });
  test('checking is empty', () => {
    expect(hashArray.isEmpty()).toBe(true);
  });
  test('adding elems', () => {
    hashArray.push('roma');
    hashArray.push('paris');
    hashArray.push('london');
    hashArray.push('new york');
    hashArray.push('tokyo');

    expect(hashArray.includes('roma')).toBe(true);
    expect(hashArray.includes('paris')).toBe(true);
    expect(hashArray.includes('london')).toBe(true);
    expect(hashArray.includes('new york')).toBe(true);
    expect(hashArray.includes('tokyo')).toBe(true);
  });

  test('checking length', () => {
    hashArray.push('roma');
    hashArray.push('paris');
    hashArray.push('london');
    hashArray.push('new york');
    hashArray.push('tokyo');
    expect(hashArray.getLength()).toBe(5);
  });

  test('removing elem', () => {
    hashArray.push('roma');
    hashArray.push('paris');
    hashArray.push('london');
    hashArray.push('new york');
    hashArray.push('tokyo');
    expect(hashArray.getLength()).toBe(5);
    expect(hashArray.isEmpty()).toBe(false);
    hashArray.remove('london');
    expect(hashArray.includes('london')).toBe(false);
    hashArray.remove('paris');
    expect(hashArray.includes('paris')).toBe(false);
  });

  test('removing from empty array', () => {
    expect(() => hashArray.remove('nonexistent')).not.toThrow();
    expect(hashArray.includes('nonexistent')).toBe(false);
  });

  test('adding and removing the same element', () => {
    hashArray.push('test');
    hashArray.remove('test');
    expect(hashArray.getLength()).toBe(0);
    expect(hashArray.isEmpty()).toBe(true);
  });

  test('resizing array', () => {
    hashArray.push('elem1');
    hashArray.push('elem2');
    hashArray.push('elem3');
    hashArray.push('elem4');
    hashArray.push('elem5');
    expect(hashArray.getLength()).toBe(5);

    // Triggering resize by adding more elements
    hashArray.push('elem6');
    hashArray.push('elem7');
    hashArray.push('elem8');
    hashArray.push('elem9');
    expect(hashArray.getLength()).toBe(9);

    // Triggering resize by removing elements
    hashArray.remove('elem1');
    hashArray.remove('elem2');
    expect(hashArray.getLength()).toBe(7);
  });
});
