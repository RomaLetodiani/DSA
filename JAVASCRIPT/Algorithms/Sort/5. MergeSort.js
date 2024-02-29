const generateArray = require('./ArrayGeneration');

// Generates an array of 500000 numbers from -1000000 to 1000000
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
// const sortedArr = mergeSort(arr);
const sortedArr = arr.sort((a, b) => a - b);
const sortedArrayString = (sortedArr) => {
  return sortedArr.join(', ');
};
const endTime = performance.now();

// It will take at least 0.12 seconds to sort the arr500K
const timeTakenInSeconds = (endTime - startTime) / 1000;

// if you want to visualize starting array just change arr to arr50K
console.log(sortedArrayString(sortedArr));
console.log('--------------------------------------------------------');
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
