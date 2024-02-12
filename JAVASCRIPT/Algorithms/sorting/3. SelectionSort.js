import { arr50K } from './arr50K.js';

const length = arr50K.length;
const middle = Math.floor(length / 2);
const arr25K = arr50K.slice(0, middle);

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

// Measure execution time
const startTime = performance.now();
const arr = arr25K;
selectionSort(arr);
const sortedArrayString = (arr) => {
  return arr.join(', ');
};
const endTime = performance.now();

// It will take at least 0.2 milliseconds to sort the arr25K
const timeTakenInSeconds = (endTime - startTime) / 1000;

console.log(sortedArrayString(arr));
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
