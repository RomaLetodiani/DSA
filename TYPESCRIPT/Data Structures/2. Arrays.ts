// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
// https://www.w3schools.com/js/js_array_methods.asp
// string[] - array of strings
// all the functions are commented
// uncomment the ones you want to use
// outputs are based on one function at a time

let myArray: Number[] = [1, 2, 3, 4, 5];

// O(1)
// .length Returns the number of elements in an array
// console.log(myArray.length); // Output: 5

// O(1) if we add one element
// O(k) if we add multiple elements where k is the number of elements we add
// push() - Adds one or more elements to the end of an array
// myArray.push(6);
// console.log(myArray); // Output: [1, 2, 3, 4, 5, 6]

// O(N) if we add one element
// O(N+K) N is the number of elements in the array and k is the number of elements we add
// concat() - creates new array from the original array and adds one or more elements
// let newArray: Number[] = myArray.concat(7, 8, 9);
// console.log(newArray); // Output: [1, 2, 3, 4, 5, 7, 8, 9]

// O(N+K) N is the number of elements in the array and k is the number of elements we add
// we can also combine two arrays
// let newArray1: Number[] = myArray.concat([10, 11, 12]);
// console.log(newArray1); // Output: [1, 2, 3, 4, 5, 10, 11, 12]

// O(1)
// Clearing the array
// myArray.length = 0;
// console.log(myArray); // Output: []

// O(N)
// indexOf() - Returns the index of the first element with the specified value, if not found return -1
// string[] O(N * M) where N is the number of strings in the array and M is the length of the string that needs to be searched
// console.log(myArray.indexOf(2)); // Output: 1

// O(N)
// splice() - Adds or removes elements from an array
// it takes three arguments
// start index, number of elements to remove, elements to add
// myArray.splice(2, 0, 10, 11, 12);
// console.log(myArray); // Output: [1, 2, 10, 11, 12, 3, 4, 5]

// O(N)
// slice() - Returns a shallow copy of a portion of an array into a new array
// it takes two arguments
// start index, end index
// console.log(myArray.slice(2, 4)); // Output: [3, 4, 5]

// O(1)
// pop() - Removes the last element from an array and returns it
// let removedElement: Number = myArray.pop();
// console.log(removedElement); // Output: 5
// console.log(myArray); // Output: [1, 2, 3, 4]

// O(N)
// shift() - Removes the first element from an array and returns it
// let removedElement: Number = myArray.shift();
// console.log(removedElement); // Output: 1
// console.log(myArray); // Output: [2, 3, 4, 5]

// O(N)
// unshift() - Adds one or more elements to the beginning of an array
// myArray.unshift(0);
// console.log(myArray); // Output: [0, 1, 2, 3, 4, 5]

// O(NlogN)
// sort() - Sorts the elements of an array
// string[] O(NlogN * M) where N is the number of strings in the array and M is the length of the string that needs to be searched
// myArray.sort();
// console.log(myArray); // Output: [1, 2, 3, 4, 5]
