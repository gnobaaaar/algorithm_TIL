### Linear Search

```javascript
var beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie'];

beasts.indexOf('Godzilla');	//all -> linear search

beasts.findIndex(function(item){
  return item === 'Godzilla';
})			//index print
	
beasts.find(function(item){
  return item === 'Godzilla';
});			//item ->Godzilla print

beasts.include('Godzilla');		//true or false
```

<br/>

### Binary Search

- 이진탐색
- 정렬된 배열에서 하나의 값을 찾아내는 데 효율적
- minIdx, maxIdx, guess

```javascript
// 특정 요소의 배열 인덱스 번호 알기
function binarySearch(array, target){
  let minIdx = 0;
  let maxIdx = array.length -1;
  
  while(minIdx <= maxIdx){
    const guess = Math.floor((minIdx+maxIdx)/2);
    
    if(array[guess] === target){
      return guess;
    }
    if(array[guess] < target){
      minIdx = guess +1;
    }else{
      maxIdx = guess -1;
    }
  }
  return -1;
}
```

<br/>

### BFS

😃 : Shortest Path, Closer Nodes

😱 : More Memory

[Ready-For-Tech-Interview/BFS & DFS.md at master · WooVictory/Ready-For-Tech-Interview (github.com)](https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/BFS %26 DFS.md)

- 너비 우선 탐색이라 하며 BFS(Breadth-First Search)라 부른다.
- 루트 노드 혹은 임의의 노드에서 시작해 인접한 노드를 먼저 탐색하는 방법.
- 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회 방법이다.
- 즉, 깊게 탐색하기 전에 넓게 탐색하는 것이다.
- 큐를 사용한다. (해당 노드의 주변부터 탐색해야 하기 때문이다.)
- 최소 비용(즉, 모든 곳을 탐색하는 것보다 최소 비용이 우선일 때)에 적합하다.

- 시간 복잡도
  - 인접 행렬 : O(V^2)
  - 인접 리스트 : O(V+E)



### DFS

😃 : Less Memory, Does Path Exist?

😱 : Can Get Slow

- 깊이 우선 탐색이며 DFS(Depth-First Search)라고 부른다.
- 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 완벽하게 탐색한다.
- 넓게 탐색하기 전에 깊게 탐색하는 것이다.
- 예를 들어, 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색을 진행하는 방법과 유사하다.
- 스택이나 재귀함수를 통해 구현한다.
- 모든 경로를 방문해야 할 경우 사용에 적합하다.

<br/>

### BFS vs DFS

```javascript
//If you know a solution is not far from the root of the tree:
BFS

//If the tree is very deep and solutions are rare, 
BFS (DFS will take long time. )

//If the tree is very wide:
DFS (BFS will need too much memory)

//If solutions are frequent but located deep in the tree
DFS

//determining whether a path exists between two nodes
DFS

//Finding the shortest path
BFS
```

<br/>

leetcode -> 98. Validate Binary Search Tree

### Daijkstra + Bellman Ford Algorithms

