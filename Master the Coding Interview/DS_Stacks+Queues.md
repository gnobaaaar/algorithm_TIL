# Stacks+Queues

😃 : Fast Operations, Fast Peek, Ordered

😱 : Slow Lookup

### stacks

lookup - O(n)

pop, push, peek - O(1)

LIFO (Last In First Out)

### queue

= waiting line

lookup - O(n)

enqueue, dequeue - O(1) : dequeue - first person in line

peek - O(1) : what's the first person in the line?

FIFO (First In First Out)

<br/>

```javascript
//Stacks

//google -> udemy -> youtube
//vs array, linked list for stacks

//Queues

// array, linked list	for queues

```

- stack은 array, linked list 둘 모두 well
  - array -> more fast
- queue는 linked list가 더 낫다
  - array는 shift가 발생하면서 비효율이 커진다 -> linear time : O(n)

<br/>



### Stack (Linked List)

```javascript
class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor(){
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }
  
  peek(){
    return this.top;
  }
  
  push(value){
		const newNode = new Node(value);
    if (this.length === 0){
      this.top = newNode;
      this.bottom = newNode;
    }else{
      const holdingPointer = this.top;
      this.top = newNode;
      this.top.next = holdingPointer;
    }
    this.length++;
    return this;
  }
  
  pop(){
    if (!this.top){
      return null;
    }
    if (this.top === this.bottom){
      this.bottom = null;
    }
    // const holdingPointer = this.top;
    this.top = this.top.next;		//uder the stack
    this.length--;
    return this;
  }
  
  //isEmpty
}

const myStack = new Stack();
// discord -> udemy -> google
```

<br/>

### Stack (Array)

```javascript
class Stack {
  constructor(){
    this.array = [];
  }
  
  peek(){
    return this.array[this.array.length-1];
  }
  
  push(value){
    this.array.push(value);
    return this;
  }
  
  pop(){
    this.array.pop();
  }
  
  //isEmpty
}

const myStack = new Stack();
// discord -> udemy -> google
```

<br/>

### Queue 

```javascript
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor(){
    this.first = null;
    this.last = null;		//last = front of line
    this.length = 0;
  }
  
  peek() {
    return this.first;
  }
  
  enqueue(value){
    const newNode = new Node(value);
    if (this.length === 0){
      this.first = newNode;
      this.last = newNode;
    }else{
      this.last.next = newNode;
      this.last = newNode;
    }
    this.length++;
    return this;
  }
  
  dequeue(){
    if (!this.first){
      return null;
    }
    if (this.first === this.last){
      this.last = null;
    }
    //const holdingPointer = this.first;
    this.first = this.first.next;
    this.length--;
    return this;
  }
  //isEmpty;
}

const myQueue = new Queue();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Jackson');
myQueue.enqueue('Shawn');
myQueue.peek();
myQueue.dequeue();
myQueue.dequeue();
```

