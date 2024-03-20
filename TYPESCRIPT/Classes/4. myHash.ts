// Mixing Operations: You might perform additional bitwise operations
// (like XOR or bit shifting) between the characters to achieve
// a better mixing of bits, ensuring a different hash code for similar strings.

const myHash = (string: string) => {
  let hash: number = 0;
  for (let i: number = 0; i < string.length; i++) {
    hash = (hash << 5) ^ (hash >> 27) ^ string.charCodeAt(i);
  }
  return hash & 0x7fffffff;
};

export default myHash;

const test_myHash = () => {
  const hashMap = new Map();

  for (let i = 0; i < 100000; i++) {
    const randomString = Math.random().toString(36).substring(2); // Generate a random string
    const hash = myHash(randomString);

    if (hashMap.has(hash)) {
      console.log(
        `Collision found on attempt ${i + 1} for hash value ${hash}: ${hashMap.get(hash)} and ${randomString}`
      );
      return;
    }

    hashMap.set(hash, randomString);
  }

  console.log('No collision found after 100,000 attempts');
};

if (require.main === module) {
  // This block will only execute when the script is run directly
  test_myHash();
}
