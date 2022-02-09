# Hash Tables

😃 : **Fast looksups**(good collision resolution needed), **Fast Inserts, Flexible Keys**

😱 : **Unordered, Slow key iteration**

> Python -> dictionary -> recently ordered

`basket.grapes = 1000` -> key/value

- key : where to find value
- hash function(black box) -> index(key), value on our memory
- value : 1000

<br/>

### Hash Function

- 암호화
- **really fasy data access**
  - MD5 Hash
  - SHA1 Hash

<br/>

### BIG O

- Insert : O(1)
- Lookup : O(1)
- Delete : O(1)
- Search : O(1)

<br/>

```javascript
let user = {
  age: 54,
  name: 'Kyle',
  magix : true,
  screa: function () {
    console.log('ahhhhhh!');
  }
}

user.age //O(1)
user.spell = 'abra kadabra';	//add -> O(1)
user.scream();	//O(1)
```

<br/>

### Hash Collision

입력은 무한하지만 출력값의 가짓값은 유한하므로(key) 반드시 해시 충돌이 발생한다(**비둘기집 원리**)

<img src="image/2525963E580F616926.png" alt="img"  />

- O(n)

- How to deal with
  - Chaining(체이닝)
    - 버켓 내에 연결리스트를 할당하여 버켓에 데이터를삽입하다가 **해시충돌 발생시 연결리스트로 데이터를 연결하는 방식**
    - **+** : 연결리스트만 사용, 단순, 채워질 수록 성능저하가 Linear하게 발생
  - Open Addressing(개방 주소법)
    - 주소값이 변하지 않는 체이닝과 달리 해시 충돌이 일어나면 다른 버켓에 데이터를 삽입
    - 선형탐색 : 다음, 몇 개를 넘긴 위치 버켓에 저장
    - 제곱탐색 : 제곱만큼
    - 이중해시 : 해시충돌시 다른 해시 함수를 한번 더 사용
    - **+** :  필요없고 지정한 메모리 외 추가 저장 공간도 없음, 삽입/삭제 오버헤드 적다, 데이터가 적을때

<br/>

<br/>

### in Javascipt

Map, Object, Set(before ES6)

```javascript
const a = new Map()	// 다양한 형식, object{} -> 기호나 문자, size사용가능
const b = new Sets()
```

### Chanllenge 

hash table -> **set, get**

```javascript
class HashTable{
  constructor(size){
    this.data = new Array(size);
  }
  _hash(key){		//_ => protected property
    let hash = 0;
    for (let i =0; i<key.length; i++){
        hash = (hash + key.charCodeAt(i) * i) % this.data.length;	
      //charCodeAt->encode
    }
    return hash;
  }
  
  set(key, value){	//O(1)
    let address = this._hash(key);
    if(!this.data[address]){
    	this.data[address] = [];
    }
    this.data[address].push([key,value]);
    return this.data;
    
  }
  
  get(key){
    let address = this._hash(key);
    const currentBucket = this.data[address];
    if (currentBucket){		//could have multiple items
      for (let i=0; i<currentBucket.length; i++){		// could be O(n)
        if(currentBucket[i][0] === key){
          return currentBucket[i][1];
        }
      }
    }	//if no collision -> O(1)
    return undefined;
  }
  
  keys(){	//BIG O..
    const keysArray = [];
    for (let i=0;i<this.data.length;i++){
      if(this.data[i]){
        keysArray.push(this.data[i][0][0])	//for chaining
      }
    }
    return keysArray;
  }
}

const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000);
myHashTable.set('apples', 10000);
myHashTable.get('grapes');
myHashTable.keys();
```

```javascript
// better keys() without collision
keys(){
  if(!this.data.length){
    return undefined
  }
  let result = [];
  for(let i=0;i<this.data.length;i++){
    //if it's not an empty memory call
    if(this.data[i] && this.data[i].length){
      //but also loop through all the potetial collsions
      if(this.data.length > 1){
        for (let j=0;j<this.data[i].length;j++){
          result.push(this.data[i][j][0])
        }
      } else{
      	result.push(this.data[i][0]) 
      }
    }
  }
  return result;
}
```

<br/>

<br/>

### Hash Tables vs Arrays

**Google Question** : what element is first repeated?

input : [2,5,1,2,3,5,1,2,4] -> output:2

input : [2,1,1,2,3,5,1,2,4] -> output:1

input : [2,3,4,5] -> output: undefined

```javascript
const inputArray = [2,5,1,2,3,5,1,2,4]

//1. naive -> wrong answer [2,5,5,2,1,2,3] -> return 2 -> how to fix this?
function firstRecurringCharater(input){
  for (let i=0; j<input.length; i++){
    for (let j=i+1; j<input.length; j++){
     if (input[i] === input[j]){
       return input[i];
     }
  }
  return undefined;
}	//O(n^2)
  //space -> O(1)
  
//2. hashTable -> add to hash table and search
function firstRecurringCharater2(input){
  let map = {};		//using hash tables
  for (let i=0; i<input.length; i++){
    if(map[input[i]] !== undefined){		//==map[2], index=0 -> false
      return input[i]
    }else{
      map[input[i]] = i;
    }
  }
  return undefined;
}	//O(n)
  
firstRecurringCharater(inputArray)
firstRecurringCharater2(inputArray)
```

