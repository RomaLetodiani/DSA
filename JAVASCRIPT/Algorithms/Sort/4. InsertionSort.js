const generateArray = require('./ArrayGeneration');

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K = generateArray(25000);

const insertionSort = (arr) => {
  for (let i = 1; i < arr.length; i++) {
    let temp = arr[i];
    let j = i - 1;
    while (j >= 0 && temp < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = temp;
  }
};

const arr = [...arr25K];

// Measure execution time
const startTime = performance.now();
insertionSort(arr);
// if you want to visualize starting array just change arr to arr25K
const sortedArrayString = arr.join(', ');
const endTime = performance.now();

// It will take at least 0.15 seconds to sort the arr25K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Insertion Sort //');
console.log('Array Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
