# Hash Tables

๐ : **Fast looksups**(good collision resolution needed), **Fast Inserts, Flexible Keys**

๐ฑ : **Unordered, Slow key iteration**

> Python -> dictionary -> recently ordered

`basket.grapes = 1000` -> key/value

- key : where to find value
- hash function(black box) -> index(key), value on our memory
- value : 1000

<br/>

### Hash Function

- ์ํธํ
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

์๋ ฅ์ ๋ฌดํํ์ง๋ง ์ถ๋ ฅ๊ฐ์ ๊ฐ์ง๊ฐ์ ์ ํํ๋ฏ๋ก(key) ๋ฐ๋์ ํด์ ์ถฉ๋์ด ๋ฐ์ํ๋ค(**๋น๋๊ธฐ์ง ์๋ฆฌ**)

<img src="image/2525963E580F616926.png" alt="img"  />

- O(n)

- How to deal with
  - Chaining(์ฒด์ด๋)
    - ๋ฒ์ผ ๋ด์ ์ฐ๊ฒฐ๋ฆฌ์คํธ๋ฅผ ํ ๋นํ์ฌ ๋ฒ์ผ์ ๋ฐ์ดํฐ๋ฅผ์ฝ์ํ๋ค๊ฐ **ํด์์ถฉ๋ ๋ฐ์์ ์ฐ๊ฒฐ๋ฆฌ์คํธ๋ก ๋ฐ์ดํฐ๋ฅผ ์ฐ๊ฒฐํ๋ ๋ฐฉ์**
    - **+** : ์ฐ๊ฒฐ๋ฆฌ์คํธ๋ง ์ฌ์ฉ, ๋จ์, ์ฑ์์ง ์๋ก ์ฑ๋ฅ์ ํ๊ฐ Linearํ๊ฒ ๋ฐ์
  - Open Addressing(๊ฐ๋ฐฉ ์ฃผ์๋ฒ)
    - ์ฃผ์๊ฐ์ด ๋ณํ์ง ์๋ ์ฒด์ด๋๊ณผ ๋ฌ๋ฆฌ ํด์ ์ถฉ๋์ด ์ผ์ด๋๋ฉด ๋ค๋ฅธ ๋ฒ์ผ์ ๋ฐ์ดํฐ๋ฅผ ์ฝ์
    - ์ ํํ์ : ๋ค์, ๋ช ๊ฐ๋ฅผ ๋๊ธด ์์น ๋ฒ์ผ์ ์ ์ฅ
    - ์ ๊ณฑํ์ : ์ ๊ณฑ๋งํผ
    - ์ด์คํด์ : ํด์์ถฉ๋์ ๋ค๋ฅธ ํด์ ํจ์๋ฅผ ํ๋ฒ ๋ ์ฌ์ฉ
    - **+** :  ํ์์๊ณ  ์ง์ ํ ๋ฉ๋ชจ๋ฆฌ ์ธ ์ถ๊ฐ ์ ์ฅ ๊ณต๊ฐ๋ ์์, ์ฝ์/์ญ์  ์ค๋ฒํค๋ ์ ๋ค, ๋ฐ์ดํฐ๊ฐ ์ ์๋

<br/>

<br/>

### in Javascipt

Map, Object, Set(before ES6)

```javascript
const a = new Map()	// ๋ค์ํ ํ์, object{} -> ๊ธฐํธ๋ ๋ฌธ์, size์ฌ์ฉ๊ฐ๋ฅ
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

