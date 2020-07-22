class Stack {
    constructor() {
      this.storage = [];
    }
  
    push(item) {
      this.storage.push(item);
    }
  
    pop() {
      return this.storage.pop();
    }
  
    peek() {
      return this.storage[this.storage.length-1];
    }
  
    isEmpty() {
      return this.storage.length === 0;
    }
  
    printContents() {
      this.storage.forEach(elem => console.log(elem));
    }
  }
  
  function sortStack(input) {
    // const -> constants, these won't be reassigned
    // let -> variables that can be reassigned
    
    // create our output stack
    const output = new Stack();
    // create our temp var = null
    let temp = null;
    // while loop over our input stack until input stack is empty
    while(!input.isEmpty()) {
      // pop off the top input element and put into a temp var
      temp = input.pop();
      // while - compare it to the peeked element of the output stack, if temp is less OR if it's empty
      while(!output.isEmpty() && temp < output.peek()) {
        // do the pop-push :tada:
        input.push(output.pop());
      }
      output.push(temp);
      // push temp onto output
    }
      
    return output;
  }
  
  const s = new Stack();
  s.push(4);
  s.push(10);
  s.push(8);
  s.push(5);
  s.push(1);
  s.push(6);
  
  const sortedStack = sortStack(s);
  
  sortedStack.printContents()
  
  
  
  
  
  
  
  
  