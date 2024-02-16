class StringBuilder {
  // O(1)
  constructor(string) {
    this.storage = [string];
    this.length = string.length;
    this.saved = string;
  }

  // O(1)
  append(string) {
    this.storage.push(string);
    this.length += string.length;
    this.saved = null;
  }

  // O(1)
  get_length() {
    return this.length;
  }

  // O(N) -> O(1)
  get_string() {
    if (this.saved) {
      return this.saved;
    } else {
      this.saved = this.storage.join('');
      return this.saved;
    }
  }
}

module.exports = StringBuilder;

function test_StringBuilder() {
  // Initialize a StringBuilder object with a starting string
  let sb = new StringBuilder('Hello');

  // Test appending strings and getting the length
  sb.append(', ');
  sb.append('World!');
  console.log(sb.get_length()); // Expected output: 13

  // Test retrieving the final string
  console.log(sb.get_string()); // Expected output: "Hello, World!"

  // Test appending an empty string
  sb.append('');
  console.log(sb.get_string()); // Expected output: "Hello, World!"

  // Test appending a very large string and measuring efficiency
  const longString = 'a'.repeat(100000); // Creating a large string
  const start = performance.now(); // Start time measurement
  sb.append(longString);
  const end = performance.now(); // End time measurement
  console.log(sb.get_length()); // Expected output: 100013
  console.log(`Time taken: ${end - start} milliseconds`);

  // Test getting the string after appending a large string
  console.log(sb.get_string().length); // Expected output: 100013
}

// Run the tests
test_StringBuilder();
