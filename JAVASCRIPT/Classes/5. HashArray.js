const myHash = (string) => {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash = (hash << 5) ^ (hash >> 27) ^ string.charCodeAt(i);
  }
  return hash & 0x7fffffff;
};

class HashArray {
  constructor() {
    this.buckets = [[], [], [], []];
    this.length = 0;
  }

  getLength() {
    return this.length;
  }

  isEmpty() {
    return this.length === 0;
  }

  push(elem) {
    const index = this.#getBucketIndex(elem);
    console.log(elem, index);
    this.buckets[index].push(elem);
    this.length += 1;

    if (this.length > this.buckets.length * 2) {
      this.#resize(this.buckets.length * 2);
    }
  }

  includes(elem) {
    const index = this.#getBucketIndex(elem);
    return this.buckets[index].includes(elem);
  }

  remove(elem) {
    if (!this.includes(elem)) {
      return;
    }
    const index = this.#getBucketIndex(elem);
    const filtered = this.buckets[index].filter((elems) => elems !== elem);
    this.buckets[index] = filtered;
    this.length -= 1;

    if (this.length < this.buckets.length / 2 && this.buckets.length > 4) {
      this.#resize(this.buckets.length / 2);
    }
  }

  #getBucketIndex(string) {
    return myHash(string) % this.buckets.length;
  }

  #resize(bucketsCount) {
    const oldBuckets = this.buckets;
    this.buckets = [];
    this.length = 0;

    for (let i = 0; i < bucketsCount; i++) {
      this.buckets.push([]);
    }

    oldBuckets.forEach((bucket) => {
      bucket.forEach((elem) => {
        this.push(elem);
      });
    });
  }
}

module.exports = HashArray;

const test_HashArray = () => {
  let ha = new HashArray();

  console.log('is empty --> ', ha.isEmpty()); // true

  ha.push('roma');
  ha.push('paris');
  ha.push('london');
  ha.push('new york');
  ha.push('tokyo');

  console.log('includes "roma" --> ', ha.includes('roma')); // true
  console.log('includes "paris" --> ', ha.includes('paris')); // true
  console.log('includes "london" --> ', ha.includes('london')); // true
  console.log('includes "new york" --> ', ha.includes('new york')); // true
  console.log('includes "tokyo" --> ', ha.includes('tokyo')); // true

  console.log('length --> ', ha.getLength()); // 5
  console.log('is empty --> ', ha.isEmpty()); // false

  ha.remove('london');
  console.log('includes "london" --> ', ha.includes('london')); // false
  console.log('length --> ', ha.getLength()); // 4

  ha.remove('paris');
  console.log('includes "paris" --> ', ha.includes('paris')); // false
  console.log('length --> ', ha.getLength()); // 3

  console.log('is empty --> ', ha.isEmpty()); // false

  ha.remove('nonexistent');
  console.log('includes "nonexistent" --> ', ha.includes('nonexistent')); // false (not present, no error)

  ha.remove('roma');
  ha.remove('new york');
  ha.remove('tokyo');

  console.log('includes "roma" --> ', ha.includes('roma')); // false
  console.log('includes "new york" --> ', ha.includes('new york')); // false
  console.log('includes "tokyo" --> ', ha.includes('tokyo')); // false

  console.log('length --> ', ha.getLength()); // 0
  console.log('is empty --> ', ha.isEmpty()); // true
  ha.remove('hello'); // does not goes on error if we try to remove non containing elem
};

test_HashArray();
