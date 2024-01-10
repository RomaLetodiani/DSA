// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
// https://www.w3schools.com/js/js_object_sets.asp

let mySet = new Set();

// O(1)
// add() - Adds a new element to the Set
mySet.add(1);
mySet.add(2);
mySet.add(3);
mySet.add(4);
mySet.add(5);
console.log(mySet); // Output: Set(5) { 1, 2, 3, 4, 5 }

// O(1)
// delete() - Removes an element from a Set
mySet.delete(1);
console.log(mySet); // Output: Set(4) { 2, 3, 4, 5 }

// O(N)
// clear() - Removes all elements from a Set
mySet.clear();
console.log(mySet); // Output: Set(0)

// O(1)
// has() - Returns whether an element is in a Set
console.log(mySet.has(1)); // false

// O(1)
// size() - Returns the number of elements in a Set
console.log(mySet.size); // 0

// O(N)
// values() - Returns a new Iterator object containing the values for each element in the Set
mySet.add(1);
mySet.add(2);
mySet.add(3);
mySet.add(4);
mySet.add(5);
console.log(mySet.values()); // Output: [Set Iterator] { 1, 2, 3, 4, 5 }

// O(N)
// entries() - Returns a new Iterator object containing the [key, value] pairs for each element in the Set
console.log(mySet.entries()); // Output: [Set Entries] { [ 1, 1 ], [ 2, 2 ], [ 3, 3 ], [ 4, 4 ], [ 5, 5 ] }

// O(N)
// keys() - Returns a new Iterator object containing the keys for each element in the Set
console.log(mySet.keys()); // Output: [Set Iterator] { 1, 2, 3, 4, 5 }

// O(N)
// forEach() - Calls a function for each element in the Set
mySet.forEach((value) => console.log(value)); // Output: 1 2 3 4 5
