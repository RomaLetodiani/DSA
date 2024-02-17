const BinarySearch = (sortedNums, target) => {
  let left = 0;
  let right = sortedNums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (sortedNums[mid] === target) {
      return mid;
    } else if (sortedNums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
};

const BinarySearchRecursion = (sortedNums, target) => {
  return recursionHelper(sortedNums, 0, sortedNums.length - 1, target);
};

const recursionHelper = (sortedNums, left, right, target) => {
  if (left > right) {
    return -1;
  }
  const mid = Math.floor((left + right) / 2);

  if (sortedNums[mid] === target) {
    return mid;
  } else if (sortedNums[mid] < target) {
    return recursionHelper(sortedNums, mid + 1, right, target);
  } else {
    return recursionHelper(sortedNums, left, mid - 1, target);
  }
};

const nums = [2, 4, 5, 17, 28, 49];

// Test Recursion
const recursionTarget = 5;
const recursionResult = BinarySearchRecursion(nums, recursionTarget);
console.log(`Recursion target ${recursionTarget} found on ${recursionResult}th index`);

// Test While Loop
const loopTarget = 49;
const loopResult = BinarySearch(nums, loopTarget);
console.log(`Loop target ${loopTarget} found on ${loopResult}th index`);

// Test Target not in Nums
const targetNotInNums = 100;
const loopResultNotInNums = BinarySearch(nums, targetNotInNums);
const recursionResultNotInNums = BinarySearchRecursion(nums, targetNotInNums);
console.log(`index of ${targetNotInNums} in nums array is ${loopResultNotInNums}`);
