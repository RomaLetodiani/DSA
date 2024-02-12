import { arr50K } from './arr50K.js';

const length = arr50K.length;
const middle = Math.floor(length / 2);
const arr25K = arr50K.slice(0, middle);

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
    if (sorted) {
      break;
    }
  }
};

// Measure execution time
const startTime = performance.now();
const arr = arr25K;
bubbleSort(arr);
const sortedArrayString = (arr) => {
  return arr.join(', ');
};
const endTime = performance.now();

// It will take at least 0.7 seconds to sort the arr25K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log(sortedArrayString(arr));
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
