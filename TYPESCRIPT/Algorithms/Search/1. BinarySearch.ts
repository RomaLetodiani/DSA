const BinarySearch = (sortedNums: number[], target: number): number | undefined => {
  let left: number = 0;
  let right: number = sortedNums.length - 1;

  while (left <= right) {
    const mid: number = Math.floor((left + right) / 2);
    if (sortedNums[mid] === target) {
      return mid;
    } else if (sortedNums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
};

const BinarySearchRecursion = (sortedNums: number[], target: number): number => {
  return recursionHelper(sortedNums, 0, sortedNums.length - 1, target);
};

const recursionHelper = (sortedNums: number[], left: number, right: number, target: number): number => {
  if (left > right) {
    return -1;
  }
  const mid: number = Math.floor((left + right) / 2);

  if (sortedNums[mid] === target) {
    return mid;
  } else if (sortedNums[mid] < target) {
    return recursionHelper(sortedNums, mid + 1, right, target);
  } else {
    return recursionHelper(sortedNums, left, mid - 1, target);
  }
};

const nums: number[] = [1, 3, 6, 14, 27, 59];

// Test Recursion
const recursionTarget: number = 6;
const recursionResult: number = BinarySearchRecursion(nums, recursionTarget);
console.log(`Recursion target ${recursionTarget} found on ${recursionResult}th index`);

// Test While Loop
const loopTarget: number = 59;
const loopResult: number | undefined = BinarySearch(nums, loopTarget);
console.log(`Loop target ${loopTarget} found on ${loopResult}th index`);

// Test Target not in Nums
const targetNotInNums: number = 100;
const loopResultNotInNums: number | undefined = BinarySearch(nums, targetNotInNums);
const recursionResultNotInNums: number = BinarySearchRecursion(nums, targetNotInNums);
console.log(`index of ${targetNotInNums} in nums array is ${loopResultNotInNums}`);
