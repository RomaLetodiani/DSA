const myHash = (string) => {
  let hash = 0;
  for (let i = 0; i < string.length; i++) {
    hash = (hash << 5) ^ (hash >> 27) ^ string.charCodeAt(i);
  }
  return hash;
};

module.exports = myHash;

const test_myHash = () => {
  const hash = myHash('hello');
  console.log(`Hash of 'hello': ${hash}`);

  const hash1 = myHash('olleh');
  console.log(`Hash of 'olleh': ${hash1}`);

  console.log(
    `Collision check: ${hash === hash1 ? 'Collision!' : 'No collision'}`
  );
};

test_myHash();
