# Linked List

😃 : Fast Insertion, Fast Deletion, Ordered, Flexible Size 

😱 : Slow Lookup, More Memory

<br/>

head -> x -> tail(last node) -> null

```javascript
const basket = ['apples', 'grapes', 'pears'];

// linked list : apples --> grapes --> pears
```

<br/>

### Why Linked List?

- start from head -> traversal -> O(n)

- prepend : O(1)
- append : O(1)
- lookup : O(n)
- insert : O(n)
- delete : O(n)

<br/>

### Pointer

```javascript
let obj1 = { a: true };
let obj2 = obj1;		//created a pointer(reference) 
// point same location in memory

obj1.a = 'booya';
delete obj1;	//console.log(obj2) -> still have 'booya'

// javascript has garbage collector
```

<br/>

### Linked List Example

```javascript
// 1 --> 10 --> (99) --> 5 --> 16

class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

//Linked List
class LinkedList {
  constructor(value){
    this.head = {
      value : value,
      next : null
    }
    this.tail = this.head;
    this.length = 1;	//optional
  }
  
  append(value){	//O(1)
    const newNode = new Node(value);
    this.tail.next = newNode;	//pointed the newNode
    this.tail = newNode;
    this.length++;
    return this;
  }
  
  prepend(value){	//O(1)
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }
  
  printList(){
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null){
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }
  
  insert(index, value){
    if (index >= this.length){
      return this.append(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index-1);	// ((*)) - *
    const holdingPointer = leader.next;	// * - ((*))
    leader.next = newNode;
    newNode.next = holdingPointer;
    this.length++;
    return this.printLitst()
  }
  
  traverseToIndex(index){
    //check prams
    let counter = 0;
    let currentNode = this.head;
    while(counter !== index){
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }
  
  remove(index){
    //check prams(...)
    const leader = this.traverseToIndex(index-1);
    const unwantedNode = leader.next;
    leader.next = unwantedNode.next;
    this.length--;
    return this.printList();
  }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.printList();
myLinkedList.insert(2, 99);

console.log(MyLinkedList);

myLinkedList.remove(2);


//error fix
if (index === 0){
	this.prepend(value);
  return this.printList();
}
```

<br/>

### Doubly Linked List

```javascript
// 1 --> 10 --> (99) --> 5 --> 16

class Node{
  constructor(value){
    this.value = value;
    this.next = null;
 		this.prev = null;
  }
}

//Linked List
class DoublyLinkedList {
  constructor(value){
    this.head = {
      value : value,
      next : null
    }
    this.tail = this.head;
    this.length = 1;	//optional
  }
  
  append(value){	//O(1)
    const newNode = new Node(value);
    newNode.prev = this.tail;
    this.tail.next = newNode;	//pointed the newNode
    this.tail = newNode;
    this.length++;
    return this;
  }
  
  prepend(value){	//O(1)
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head.prev = newNode;
    this.head = newNode;
    this.length++;
    return this;
  }
  
  printList(){
    const array = [];
    let currentNode = this.head;
    while(currentNode !== null){
      array.push(currentNode.value);
      currentNode = currentNode.next;
    }
    return array;
  }
  
  insert(index, value){
    if (index >= this.length){
      return this.append(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index-1);
    const follower = leader.next;
    leader.next = newNode;
    newNode.prev = leader;
    newNode.next = follower;
    follower.prev = newNode;
    this.length++;
    return this.printLitst()
  }
  
  traverseToIndex(index){
    //check prams
    let counter = 0;
    let currentNode = this.head;
    while(counter !== index){
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }
  
  remove(index){
    //check prams(...)
    const leader = this.traverseToIndex(index-1);
    const unwantedNode = leader.next;
    unwantedNode.next.prev = leader;
    leader.next = unwantedNode.next;
    this.length--;
    return this.printList();
  }
  
  //how to reverse?
  reverse(){				
    if(!this.head.next){
      return this.head;
    }
    let first = this.head;
    this.tail = this.head;
    let second = first.next;
    while(second){
      const temp = second.next;
      second.next = first;
      first = second;
      second = temp;
    }
    this.head.next = null;
    this.head = first;
    return this.printList();
  }
}

const myLinkedList = new DoublyLinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.printList();
myLinkedList.insert(2, 99);
console.log(MyLinkedList);

myLinkedList.remove(2);
myLinkedList.reverse();
console.log(MyLinkedList);
```

<br/>

