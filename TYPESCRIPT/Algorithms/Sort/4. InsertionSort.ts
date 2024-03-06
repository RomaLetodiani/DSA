import { generateArray } from './ArrayGeneration';

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K: number[] = generateArray(25000);

const insertionSort = (arr: number[]) => {
  for (let i: number = 1; i < arr.length; i++) {
    let temp: number = arr[i];
    let j: number = i - 1;
    while (j >= 0 && temp < arr[j]) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = temp;
  }
};

const arr: number[] = [...arr25K];

// Measure execution time
const startTime: number = performance.now();
insertionSort(arr);
// if you want to visualize starting array just change arr to arr25K
const sortedArrayString: string = arr.join(', ');
const endTime: number = performance.now();

// It will take at least 0.15 seconds to sort the arr25K
const timeTakenInSeconds: number = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Insertion Sort //');
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
