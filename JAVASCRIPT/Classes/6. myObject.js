// Mixing Operations: You might perform additional bitwise operations
// (like XOR or bit shifting) between the characters to achieve
// a better mixing of bits, ensuring a different hash code for similar strings.

const myHash = (string) => {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash = (hash << 5) ^ (hash >> 27) ^ string.charCodeAt(i);
  }
  return hash & 0x7fffffff;
};

class MyObject {
  constructor() {
    this.buckets = [[], [], [], []]; // [[[k,v]], [], [], []]
    this.length = 0;
  }

  getLength() {
    return this.length;
  }

  isEmpty() {
    return this.length === 0;
  }

  includes(key) {
    return this.get(key) !== undefined;
  }

  get(key) {
    const index = this.#getBucketIndex(key);
    const bucket = this.buckets[index];

    for (const pair of bucket) {
      if (pair[0] === key) {
        return pair[1];
      }
    }
    return;
  }

  set(key, value) {
    const index = this.#getBucketIndex(key);

    this.buckets[index].forEach((pair) => {
      if (pair[0] === key) {
        pair[1] = value;
        return;
      }
    });

    this.buckets[index].push([key, value]);
    this.length += 1;

    if (this.length > this.buckets.length * 2) {
      this.#resize(this.buckets.length * 2);
    }
  }

  remove(key) {
    if (!this.includes(key)) {
      return;
    }
    const index = this.#getBucketIndex(key);
    const bucket = this.buckets[index];

    const filtered = bucket.filter((pair) => pair[0] !== key);
    this.buckets[index] = filtered;

    this.length -= 1;

    if (this.length < this.buckets.length / 2 && this.buckets.length > 4) {
      this.#resize(this.buckets.length / 2);
    }
  }

  #resize(bucketCount) {
    const oldBuckets = this.buckets;
    this.buckets = [];
    this.length = 0;

    for (let i = 0; i < bucketCount; i++) {
      this.buckets.push([]);
    }

    oldBuckets.forEach((bucket) => {
      bucket.forEach((pair) => {
        this.set(pair[0], pair[1]);
      });
    });
  }

  #getBucketIndex(key) {
    return myHash(key) % this.buckets.length;
  }
}

module.exports = MyObject;
