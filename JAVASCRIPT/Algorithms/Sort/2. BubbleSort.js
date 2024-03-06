const generateArray = require('./ArrayGeneration');

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K = generateArray(25000);

const bubbleSort = (arr) => {
  for (let i = 0; i < arr.length; i++) {
    let sorted = true;
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        sorted = false;
      }
    }
    if (sorted) break;
  }
};

const arr = [...arr25K];

// Measure execution time
const startTime = performance.now();
bubbleSort(arr);
// if you want to visualize starting array just change arr to arr25K
const sortedArrayString = arr.join(', ');
const endTime = performance.now();

// It will take at least 0.7 seconds to sort the arr25K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Bubble Sort //');
console.log('Array Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
