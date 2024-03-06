import { generateArray } from './ArrayGeneration';

// Generates an array of 25000 random numbers from -20000 to 20000
const arr25K: number[] = generateArray(25000);

const bubbleSort = (arr: number[]) => {
  for (let i: number = 0; i < arr.length; i++) {
    let sorted: boolean = true;
    for (let j: number = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        let temp: number = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        sorted = false;
      }
    }
    if (sorted) break;
  }
};

const arr: number[] = [...arr25K];

// Measure execution time
const startTime: number = performance.now();
bubbleSort(arr);
// if you want to visualize starting array just change arr to arr25K
const sortedArrayString: string = arr25K.join(', ');
const endTime: number = performance.now();

// It will take at least 0.7 seconds to sort the arr25K
const timeTakenInSeconds: number = (endTime - startTime) / 1000;

console.log('[', sortedArrayString, ']');
console.log('--------------------------------------------------------');
console.log('// Stats of Bubble Sort //');
console.log('Length --> ', arr.length);
console.log('Time taken:', timeTakenInSeconds, 'seconds');
