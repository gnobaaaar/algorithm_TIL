## 깊이 우선 탐색 (Depth-First Search)

<br />

### 그래프 예와 파이썬 표현
<img src="image/dfsgraph.png" width=700>

<br />

### DFS 알고리즘 구현

- 자료구조 스택과 큐를 활용함
  - need_visit **스택**과 visited 큐, 두 개의 자료 구조를 생성

> BFS 자료구조는 두 개의 큐를 활용하는데 반해, DFS 는 스택과 큐를 활용한다는 차이가 있음을 인지해야 함

```python
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
```

