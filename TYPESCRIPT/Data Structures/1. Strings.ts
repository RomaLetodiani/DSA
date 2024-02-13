// https://www.w3schools.com/js/js_string_methods.asp
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String

// O(1)
let nameStr: string = 'World';
console.log(`Hello, ${name}!`);

// O(min(M, K)) ~ O(N)
// startswith()	Returns true if the string starts with the specified value
// endswith() - Returns true if the string ends with the specified value
let testStr: string;
testStr = 'abcdef'; // M - len of testStr
console.log(testStr.startsWith('abc')); // K - len of substring

// O(M * K) ~ O(N^2)
// includes() - Returns true if the string contains the specified value
// indexOf() - Searches the string for a specified value and returns the position of where it was found (raises an exception if the value is not found)
// lastIndexOf() - Searches the string for a specified value and returns the last position of where it was found (raises an exception if the value is not found)
testStr = 'abcdabcd'; // M - len of testStr
console.log(testStr.indexOf('bc')); // K - len of substring

// O(M * min(L, K)) ~ O(N^2)
// replace() - Returns a string where a specified value is replaced with another value
testStr = 'abcdabcd'; // M - length of testStr
let replaced: string = testStr.replace('bc', 'TTT'); // K - length of replacement, L - length of substring
console.log(replaced); // Output: "aTTTdabcd"

// O(M * K) ~ O(N^2)
// split() - Splits the string at the specified separator, and returns a list
// splitlines() - Splits the string at line breaks and returns a list
testStr = 'abcdabcd'; // M - len of testStr
console.log(testStr.split('bc')); // K - len of substring

// O(N)
// join() - Converts the elements of an iterable into a string
let arr: string[] = ['11', '22', '33'];
console.log(arr.join('++')); // N - len of iterable

// O(N)
// toUpperCase() - Converts a string into upper case
// toLowerCase() - Converts a string into lower case
let text: string = 'abcdabcd';
console.log(text.toUpperCase()); // Output: "ABCDABCD"
console.log(text.toLowerCase()); // Output: "abcdabcd"
