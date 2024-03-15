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

const test_myHash = () => {
  const hash: number = myHash('hello');
  console.log(`Hash of 'hello': ${hash}`);

  const hash1: number = myHash('olleh');
  console.log(`Hash of 'olleh': ${hash1}`);

  console.log(`Collision check: ${hash === hash1 ? 'Collision!' : 'No collision'}`);
};

if (require.main === module) {
  // This block will only execute when the script is run directly
  test_myHash();
}

export default myHash;
