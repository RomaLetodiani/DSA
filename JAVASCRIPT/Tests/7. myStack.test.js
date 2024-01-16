const MyStack = require('../Classes/7. myStack'); // Adjust the import path based on your project structure

describe('Stack', () => {
  let stack;

  beforeEach(() => {
    stack = new MyStack();
  });

  test('isEmpty and top method for an empty stack', () => {
    expect(stack.isEmpty()).toBe(true);
    expect(stack.top()).toBe(null);
  });

  test('pushing multiple elements', () => {
    stack.push(5);
    expect(stack.isEmpty()).toBe(false);
    expect(stack.size()).toBe(1);
    expect(stack.top()).toBe(5);

    stack.push(10);
    stack.push(15);
    expect(stack.size()).toBe(3);
    expect(stack.top()).toBe(15);
  });

  test('popping elements', () => {
    stack.push(5);
    stack.push(10);
    stack.push(15);

    stack.pop();
    expect(stack.size()).toBe(2);
    expect(stack.top()).toBe(10);

    stack.pop();
    expect(stack.size()).toBe(1);
    expect(stack.top()).toBe(5);

    stack.pop();
    expect(stack.size()).toBe(0);
    expect(stack.top()).toBe(null);
    expect(stack.isEmpty()).toBe(true);
  });

  test('popping element from empty stack', () => {
    expect(stack.pop()).toBe(undefined);
  });

  test('adding elements after emptying the stack', () => {
    stack.push(20);
    stack.push(25);

    expect(stack.size()).toBe(2);
    expect(stack.top()).toBe(25);
  });
});
