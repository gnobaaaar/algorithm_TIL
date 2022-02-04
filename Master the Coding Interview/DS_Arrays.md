# Arrays

- **lookup, push -> O(1)**

- **Insert, delete -> O(n)**

<br/>

```javascript
const strings = ['a', 'b', 'c', 'd'];
//4 * 4 = 16 byes of storage
//computer knows element's index

//search
strings[2]	//O(1)

//push
strings.push('e'); // O(1) because last index
console.log(strings)

//pop
strings.pop() // O(1) because computer knows where

//unshift
strings.unshift('x'); // beginning of array, 다른 요소들이 이동해야한다 -> O(n) : looping

//splice
strings.splice(2, 0, 'alien') // x, a, alien, b, c -> O(n/2) = O(n)
```

- python
  - 인덱싱 [1:3] -> index 1,2
  - add : a.append(index-num) or a.insert(index, item)
  - delete : a.remove(idx), del a[idx]
  - sort : a.sort() -> 원본도 변경
  - a.sorted(reverse=True)

<br/>

<br/>

### Static Arrays vs Dynamic Arrays

Stattic : C++

Dynamic Arrays : Javascript -> **append can be O(n)**

- 전체 공간을 복사하여