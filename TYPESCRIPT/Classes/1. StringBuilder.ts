class StringBuilder {
  storage: string[];
  length: number;
  saved?: string;

  constructor(str: string) {
    this.storage = [str];
    this.length = str.length;
    this.saved = str;
  }

  append(str: string): void {
    this.storage.push(str);
    this.length += str.length;
    this.saved = undefined;
  }

  get_length(): number {
    return this.length;
  }

  get_string(): string {
    if (this.saved) {
      return this.saved;
    } else {
      this.saved = this.storage.join('');
      return this.saved;
    }
  }
}

export default StringBuilder;

const test_StringBuilder = (): void => {
  // Initialize a StringBuilder object with a starting string
  const sb: StringBuilder = new StringBuilder('Hello');

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
  const longString: string = 'a'.repeat(100000); // Creating a large string
  const start: number = performance.now(); // Start time measurement
  for (let i: number = 0; i < 100000; i++) {
    sb.append(longString[i]);
  }
  const end: number = performance.now(); // End time measurement
  console.log(sb.get_length()); // Expected output: 100013
  console.log(`Time taken: ${end - start} milliseconds`);

  // Test getting the string after appending a large string
  console.log(sb.get_string().length); // Expected output: 100013
};

// Run the tests
test_StringBuilder();
