const generateArray = require('./ArrayGeneration');

// Generates an array of 500000 random numbers from -1000000 to 1000000
const arr500K = generateArray(500000, -1000000, 1000000);

const mergeHelper = (arr1, arr2) => {
  const result = [];

  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else {
      result.push(arr2[j]);
      j++;
    }
  }
  result.push(...arr1.slice(i));
  result.push(...arr2.slice(j));

  return result;
};

const mergeSort = (arr) => {
  if (arr.length < 2) {
    return arr;
  }

  const middle_index = arr.length / 2;
  const left = mergeSort(arr.slice(0, middle_index));
  const right = mergeSort(arr.slice(middle_index));

  return mergeHelper(left, right);
};

const arr = [...arr500K];

// Measure execution time
const startTime = performance.now();
const sortedArr = mergeSort(arr);
// if you want to visualize starting array just change sortedArr to arr500K
const sortedArrayString = sortedArr.join(', ');
const endTime = performance.now();

// It will take at least 0.2 seconds to sort the arr500K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Merge Sort //');
console.log('Array Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
