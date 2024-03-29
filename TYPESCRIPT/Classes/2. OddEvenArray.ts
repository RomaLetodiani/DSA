class OddEvenArray {
  odds: number[];
  evens: number[];

  constructor() {
    this.odds = [];
    this.evens = [];
  }

  // O(1)
  length(): number {
    return this.odds.length + this.evens.length;
  }

  // O(1)
  add(num: number): void {
    if (num % 2 == 0) {
      this.evens.push(num);
    } else {
      this.odds.push(num);
    }
  }

  // O(1)
  getOdds(): number[] {
    return this.odds;
  }

  // O(1)
  getEvens(): number[] {
    return this.evens;
  }
}

export default OddEvenArray;

function test_OddEvenArray(): void {
  // Initialize an OddEvenArray object
  let oea: OddEvenArray = new OddEvenArray();

  // Test adding numbers and getting the length
  oea.add(1);
  oea.add(2);
  oea.add(3);
  console.log(oea.length()); // Expected output: 3

  // Test retrieving even numbers
  console.log(oea.getEvens()); // Expected output: [2]

  // Test retrieving odd numbers
  console.log(oea.getOdds()); // Expected output: [1, 3]

  // Add more test cases as needed...
}

// Run the tests
if (require.main === module) {
  // This block will only execute when the script is run directly
  test_OddEvenArray();
}
