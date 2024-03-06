/**
 * Generates an array of random integers within a specified range.
 * @param {number} [size=10000] The size of the array to be generated.
 * @param {number} [min=-20000] The minimum value of the random integers to be generated.
 * @param {number} [max=20000] The maximum value of the random integers to be generated.
 * @returns {number[]} An array of random integers within the specified range.
 */
const generateArray = (size = 10000, min = -20000, max = 20000) => {
  return Array.from({ length: size }, () => Math.floor(Math.random() * (max - min + 1)) + min);
};

module.exports = generateArray;

// Example usage
// Generates an array of 50000 random numbers from -1000000 to 1000000
const arr50K = generateArray(50000, -1000000, 1000000);
console.log('[', arr50K.join(', '), ']');
console.log('--------------------------------------------------------');
console.log('Array Length', arr50K.length);

// Run this command in the terminal
// node '.\Algorithms\Sort\ArrayGeneration.ts'
