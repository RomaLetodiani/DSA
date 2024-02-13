// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects

// O(1)
// Creating an object.
const myObject: {
  [key: string]: string;
} = {};
console.log(myObject);

// O(1)
// Adding/Updating a property.
myObject.key = 'value';
myObject['key 2'] = 'value 2';
console.log(myObject);

// O(1)
// Accessing a property.
const value: string = myObject.key;
console.log(value);

// O(1)
// Checking if a property exists.
const exists: boolean = 'key' in myObject;
console.log(exists);

// O(1)
// Deleting a property.
// delete myObject.key;

// O(N)
// Getting object keys.
const keys: string[] = Object.keys(myObject);
console.log(keys);

// O(N)
// Getting object values.
const values: string[] = Object.values(myObject);
console.log(values);

// O(N)
// Getting object entries.
const entries: [string, string][] = Object.entries(myObject);
console.log(entries);

// O(1) (for built-in data structures like Map and Set)
// Checking object size.
const size: number = Object.keys(myObject).length;
console.log(size);
