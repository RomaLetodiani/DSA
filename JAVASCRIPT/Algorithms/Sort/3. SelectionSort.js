const generateArray = require('./ArrayGeneration');

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K = generateArray(25000);

const selectionSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      const temp = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
    }
  }
};

const arr = [...arr25K];

// Measure execution time
const startTime = performance.now();
selectionSort(arr);
// if you want to visualize starting array just change arr to arr25K
const sortedArrayString = arr.join(', ');
const endTime = performance.now();

// It will take at least 0.2 seconds to sort the arr25K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Selection Sort //');
console.log('Array Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
