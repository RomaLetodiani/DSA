import { generateArray } from './ArrayGeneration';

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K: number[] = generateArray(25000);

const selectionSort = (arr: number[]): void => {
  for (let i: number = 0; i < arr.length; i++) {
    let minIndex: number = i;
    for (let j: number = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex !== i) {
      const temp: number = arr[i];
      arr[i] = arr[minIndex];
      arr[minIndex] = temp;
    }
  }
};

const arr: number[] = [...arr25K];

// Measure execution time
const startTime: number = performance.now();
selectionSort(arr);
const sortedArrayString: string = arr.join(', ');
const endTime: number = performance.now();

// It will take at least 0.2 seconds to sort the arr25K
const timeTakenInSeconds: number = (endTime - startTime) / 1000;

// if you want to visualize starting array just change arr to arr25K
console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Selection Sort //');
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
