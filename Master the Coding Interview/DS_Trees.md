# Trees

- 계층구조
- Parent-Child relationship
- Subtree
- DOM -> Tree Data Structure
- linked list -> 트리의 일종, one path

<br/>

### binary Trees

- 각 노드는 0, 1, 2 (자식)노드를 가진다

```javascript
function BinaryTreeNode(value){
  this.value = value;
  this.left = null;
  this.right = null;
}
```

<img src="image/image-20220213191459188.png" alt="image-20220213191459188" style="zoom:50%;" />

**Perfect Binary Tree(포화 이진 트리)**

- 효율적
- next level -> double nodes (x2)
- 마지막 노드의 수 = 나머지 (레벨)노드의 수 +1
- lookup, insert, delete -> O(log N)
- Level 0의 노드의 수 : 2^0 = 1
- Level 1의 노드의 수 : 2^1 = 2
- 총 노드의 수 : 2^높이(level+1) - 1
  - log nodes = height

<br/>

### binary search tree

😃 : Better than O(n), Ordered, Flexible Size

😱 : No O(1) Operation 

lookup, insert, delete -> O(log N)

Insert -> traversing nodes

1. currentnode 보다 right child node가 더 크다(left는 더 작아진다)
2. node는 두 개까지 자식노드를 가질 수 있다 -> lookup

<br/>

### balanced vs unbalanced BST

<img src="image/image-20220213213404803.png" alt="image-20220213213404803" style="zoom:50%;" />

unbalanced BST -> lookup, insert, delete -> O(n) -> how do you balanced?

-> AVL, Red Black Tree ...

<br/>

```javascript
class Node{
  constructor(value){
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySearchTree{
  constructor(){
    this.root = null;
  }
  
  insert(value){
  
  }
  
  lookup(value){
    
  }
  
  //remove
}

const tree = new BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
JSON.stringify(traverse(tree.root))

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
```

