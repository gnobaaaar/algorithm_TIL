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

### Graph + Tree
