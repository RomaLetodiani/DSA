// Stack - LIFO structure (last in first out)

class Stack {
  // O(1)
  constructor() {
    this.storage = [];
  }

  // O(1)
  size() {
    return this.storage.length;
  }

  // O(1)
  isEmpty() {
    return this.size() === 0;
  }

  // O(1) @
  push(elem) {
    this.storage.push(elem);
  }

  // O(1)
  pop() {
    if (this.isEmpty()) {
      return;
    }
    return this.storage.pop();
  }

  // O(1)
  top() {
    if (this.isEmpty()) {
      return null;
    }
    return this.storage[this.storage.length - 1];
  }
}

const testStack = () => {
  const stack = new Stack();

  console.log('"test isEmpty and top method for an empty stack"');
  console.log('--------'); // --------
  console.log('is empty -> ', stack.isEmpty()); // true
  console.log('top -> ', stack.top()); // null

  console.log('--------'); // --------
  console.log('"test pushing multiple elements"');
  console.log('--------'); // --------

  console.log('pushed 5');
  stack.push(5);
  console.log('is empty -> ', stack.isEmpty()); // false
  console.log('size -> ', stack.size()); // 1
  console.log('top -> ', stack.top()); // 5
  console.log('pushed 10 and 15');
  stack.push(10);
  stack.push(15);
  console.log('size -> ', stack.size()); // 3
  console.log('top -> ', stack.top()); // 15

  console.log('--------'); // --------
  console.log('"test popping elements"');
  console.log('--------'); // --------

  console.log('pop elem');
  stack.pop();
  console.log('size -> ', stack.size()); // 2
  console.log('top -> ', stack.top()); // 10

  console.log('pop elem');
  stack.pop();
  console.log('size -> ', stack.size()); // 1
  console.log('top -> ', stack.top()); // 5

  console.log('pop elem');
  stack.pop();
  console.log('size -> ', stack.size()); // 0
  console.log('top -> ', stack.top()); // null
  console.log('is empty -> ', stack.isEmpty()); // true

  console.log('--------'); // --------
  console.log('"test popping element from empty stack"');
  console.log('--------'); // --------

  console.log('does not error on pop and returns ->', stack.pop()); // undefined

  console.log('--------'); // --------
  console.log('"Test adding elements after emptying the stack"');
  console.log('--------'); // --------

  stack.push(20);
  stack.push(25);

  console.log('size -> ', stack.size()); // 2
  console.log('top -> ', stack.top()); // 25
};

testStack();
