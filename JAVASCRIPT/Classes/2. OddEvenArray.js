class OddEvenArray {
  constructor() {
    this.odds = [];
    this.evens = [];
  }

  // O(1)
  length() {
    return this.odds.length + this.evens.length;
  }

  // O(1)
  add(num) {
    if (num % 2 == 0) {
      this.evens.push(num);
    } else {
      this.odds.push(num);
    }
  }

  // O(1)
  getOdds() {
    return this.odds;
  }

  // O(1)
  getEvens() {
    return this.evens;
  }
}

module.exports = OddEvenArray;

function test_OddEvenArray() {
  // Initialize an OddEvenArray object
  let oea = new OddEvenArray();

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
test_OddEvenArray();
