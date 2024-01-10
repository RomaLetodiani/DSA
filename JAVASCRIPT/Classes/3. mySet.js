// Mixing Operations: You might perform additional bitwise operations
// (like XOR or bit shifting) between the characters to achieve
// a better mixing of bits, ensuring a different hash code for similar strings.

const myHash = (string) => {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash = (hash << 5) ^ (hash >> 27) ^ string.charCodeAt(i);
  }
  return hash;
};

class MySet {
  constructor() {
    this.buckets = [[], [], [], []];
    this.length = 0;
  }

  // O(1) @
  get(string) {
    if (this.has(string)) {
      const index = this.buckets[this.#getBucketIndex(string)].indexOf(string);
      return this.buckets[this.#getBucketIndex(string)][index];
    }
  }

  // O(1)
  size() {
    return this.length;
  }

  // O(1) @
  add(string) {
    if (this.has(string)) {
      return;
    }
    this.buckets[this.#getBucketIndex(string)].push(string);
    this.length++;
    if (this.length > this.buckets.length * 2) {
      this.#resize(this.buckets.length * 2);
    }
  }

  // O(1) @
  delete(string) {
    if (!this.has(string)) {
      return;
    }
    this.buckets[this.#getBucketIndex(string)].splice(
      this.buckets[this.#getBucketIndex(string)].indexOf(string),
      1
    );
    this.length--;
    if (this.length < this.buckets.length / 2 && this.buckets.length > 4) {
      this.#resize(len(this.buckets) / 2);
    }
  }

  // O(1) @
  has(string) {
    if (!this.buckets[this.#getBucketIndex(string)]) {
      return false;
    }
    return this.buckets[this.#getBucketIndex(string)].includes(string);
  }

  // O(1)
  clear() {
    this.buckets = [[], [], [], []];
    this.length = 0;
    this.#resize(this.buckets.length);
  }

  // O(N)
  values() {
    const values = [];
    for (let i = 0; i < this.buckets.length; i++) {
      for (let j = 0; j < this.buckets[i].length; j++) {
        values.push(this.buckets[i][j]);
      }
    }
    return values;
  }

  // O(N)
  #resize(bucketsNum) {
    const oldBuckets = this.buckets;
    this.buckets = [];
    this.length = 0;

    for (let i = 0; i < bucketsNum; i++) {
      this.buckets.push([]);
    }

    for (let i = 0; i < oldBuckets.length; i++) {
      for (let j = 0; j < oldBuckets[i].length; j++) {
        this.add(oldBuckets[i][j]);
      }
    }
  }

  // O(N)
  #getBucketIndex(string) {
    return myHash(string) % this.buckets.length;
  }
}

module.exports = MySet;

const testMySet = () => {
  const mySet = new MySet();
  mySet.add('hello');
  mySet.add('world');
  mySet.add('how');
  mySet.add('are');
  mySet.add('you');
  console.log('size ->', mySet.size()); // 5

  console.log('values ->', mySet.values()); // [ 'world', 'are', 'you', 'hello', 'how' ]

  console.log("has 'world' ->", mySet.has('world')); // true

  console.log("get 'how' ->", mySet.get('how')); // true

  mySet.delete('world');
  console.log('values after delete ->', mySet.values()); // [ 'are', 'you', 'hello', 'how' ]

  console.log("has 'world' ->", mySet.has('world')); // false

  mySet.clear();
  console.log('values after clear ->', mySet.values()); // []

  console.log('has "hello" ->', mySet.has('hello')); // false

  console.log('size ->', mySet.size()); // 0

  console.log('get "how" ->', mySet.get('how')); // undefined
};

testMySet();
