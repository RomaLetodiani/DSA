/**
 * Generates an array of random integers within a specified range.
 * @param size The size of the array to be generated. Default is 10000.
 * @param min The minimum value of the random integers to be generated. Default is -20000.
 * @param max The maximum value of the random integers to be generated. Default is 20000.
 * @returns An array of random integers within the specified range.
 */
export const generateArray = (size: number = 10000, min: number = -20000, max: number = 20000): number[] => {
  return Array.from({ length: size }, () => Math.floor(Math.random() * (max - min + 1)) + min);
};

// Checking if require.main === module to prevent running the example usage in other files
if (require.main === module) {
  // Example usage
  // Generates an array of 50000 random numbers from -1000000 to 1000000
  const arr50K: number[] = generateArray(50000, -1000000, 1000000);
  console.log('[', arr50K.join(', '), ']');
  console.log('--------------------------------------------------------');
  console.log('Array Length:', arr50K.length);
}

// Run this command in the terminal
// ts-node '.\Algorithms\Sort\ArrayGeneration.ts'
