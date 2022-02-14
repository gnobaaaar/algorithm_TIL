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

**remove is not easy to understand, focus on insert, lookup**

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
  	const newNode = new Node(value);
    if (this.root === null){
      this.root = newNode;
    }else{
      let currentNode = this.root;	//ready to traverse(point)
      while(true){
        if(value < currentNode.value){
          //Left
          if(!currentNode.left){
            currentNode.left = newNode;
            return this;
          }
          currentNode = currentNode.left;
        }else{
          //Right
          if(!currentNode.right){
            currentNode.right = newNode;
            return this;
          }
          currentNode = currentNode.right;
        }
      }
    }
  }
  
  lookup(value){
    if (!this.root){
      return false;
    }
    let currentNode = this.root;
    while(currentNode){
      if(value < currentNode.value){
        currentNode = currentNode.left;
      }else if(value > currentNode.value){
        currentNode = currentNode.right;
      }else if (currentNode.value === value){
        return currentNode;
      }
    }
    return false;
  }
  
  //remove
  remove(value){
    if(!this.root){
      return false;
    }
    let currentNode = this.root;
    let parentNode = null;
    while(currentNode){
      if(value < currentNode.value){
        parentNode = currentNode;
        currentNode = currentNode.left;
      }else if(value > currentNode.value){
        parentNode = currentNode;
        currentNode = currentNode.right;
      }else if(value === currentNode.value){
        //we have a match, get to work!
        
        //option1 : No right child
        if (currentNode.right === null){
          if (parentNode === null){
            this.root = currentNode.left;
          }else{
            // if parent > current value, make current left child a child of a parent
            if(currentNode.value < parentNode.value){
              parentNode.left = currentNode.left;
            }	//if parent < current value, make left child a right child of a parent
            else if (currentNode.value > parentNode.value){
              parentNode.right = currentNode.left;
            }
          }
        }//option2 : Right child which doesnt have a left child 
        else if (currentNode.right.left === null){
          if(parentNode === null){
            this.root = currentNode.left;
          } else{
            currentNode.right.left = currentNode.left;
            
            //if parent > current, make right child of the left the parent
            if (currentNode.value < parentNode.value){
              parentNode.left = currentNode.right;
            }
            //if parent < current, make right child a right child of the parent
            else if (currentNode.value > parentNode.value){
              parentNode.right = currentNode.right;
            }
          }
        }//option3 : Right child that has a left child 
        else{
          // find the right child's left most child
          let leftmost = currentNode.right.left;
          let leftmostParent = currentNode.right;
          while(leftmost.left !== null){
            leftmostParent = leftmost;
            leftmost = leftmost.left;
          }
          
          //parent's left subtree is now leftmost's right subtree
          leftmostParent.left = leftmost.right;
          leftmost.left = currentNode.left;
          leftmost.right = currentNode.right;
          
          if(parentNode === null){
            this.root = leftmost;
          }
          else{
            if (currentNode.value < parentNode.value){
              parentNode.left = leftmost;
            }else if (currentNode.value > parentNode.value){
              parentNode.right = leftmost;
            }
          }
        }
        return true;
      }
    }
  }
}

const tree = new BinarySearchTree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
//JSON.stringify(traverse(tree.root))

//     9
//  4     20
//1  6  15  170

//later...
function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
```

<br/>

