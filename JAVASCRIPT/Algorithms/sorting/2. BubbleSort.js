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

const arr = arr25K;
bubbleSort(arr);
console.log(arr);
