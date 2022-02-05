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

<br/>

<br/>

### Javascript Concepts

- non primitive type
- created by programmer

```javascript
// reference type
var object1 = Box1	// box1 references
var object2 = object1 //refrences box1	
var object3 = Box3	//box3

[] === [] 	//false

//context vs scope
console.log(this)

//instantiation
class Playaer{
  constructor(name, type){
    console.log(this);		// -> Wizard() -> we created new Wizard
    this.name = name;
    this.type = type;
  }
  introduce(){
    console.log(`Hi I am ${this.name}, I'm a ${this.type}`);
  }
}

class Wizard extends Player{
  constructor(name, type){
    super(name, type)		//must call
  }
  play(){
    console.log(`WWWWEEEEE I'am ${this.type}`)
  }
}

const wizard1 = new Wizard('Shelly', 'Healer');
const wizard2 = new Wizard('Shawn', 'Dark Magic');
```

<br/>

<br/>

### Imprementing An Array

How to build One

```javascript
class MyArray{
  constructor(){
    this.length = 0;
    this.data = {};		//object
  }
  
  get(index){
    return this.data[index];
  }
  
  push(item){
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop(){
    const lastItem = this.data[this.length-1];
    delete this.data[this.length-1];
    this.length--;
    return lastItem;
  }

  delete(index){
    const item = this.data[index];
    this.shiftItems(index);
    return lastItem;
  }

  shiftItems(index){
    for (let i =index; i <this.length-1; i++){
      this.data[i] = this.data[i+1];  
    }
    // how to delete last item?
    delete this.data[this.length-1];
    this.length--;
  }
}

const newArray = new MyArray();
newArray.push('hi');
newArray.push('you');
newArray.push('!');
// newArray.pop();
// newArray.pop();
newArray.delete(0);
newArray.push('are');
newArray.push('nice');
newArray.delete(1);
console.log(newArray);
```

<br/>

<br/>

### Strings and Array

>  Strings is sort of Array

**Can you create a function that reverses a string(문자열 거꾸로)**

`Hi My name is Anrei`

```javascript
// for loop
function reverse(str){
  // check input
  if (!str || str.length < 2 || typeof str !== 'string'){
		return 'hmm that is not good';
  }
  
  const backwards = [];
  const totalItems = str.length -1;
  for (let i = totalItems; i >= 0; i--){
    backwards.push(str[i]);
  }
  
  return backwards.join('')
}

// reverse()
function reverse2(str){
  return str.split('').reverse().join('');
}

// ES6
const reverse3 = str => str.split('').reverse().join('');

// ES6 ...
const reverse3 = str => [...str].reverse().join('');



reverse('Hi My name is Anrei');
```

**Python**

```python
# reverse
stringList = list(str)
stringList.reverse()
newStr = ''.join(stringList)

# [::-1]
newStr = str[::-1]

# for loop
reverseStr = ''
for word in str:
  reverseStr = word + reverseStr
```

<br/>

<br/>

### Merge Sorted Array

**Q : [0, 3, 4, 31], [4, 6, 30] -> [0, 3, 4, 4, 6, 30, 31]**

```javascript
function mergeSortedArray(arr1, arr2){
  const mergedArray = [];
  let array1Item = array1[0];
  let array2Item = array2[0];
  let i = 1;
  let j = 1;
  
  // Check input
  if (array1.length === 0){
    return array2
  }
  if (array2.length === 0){
    return array1
  }
  
  // arrays could not be compare each other bacause of their own length.
  while (array1Item || array2Item){
    if (!array2Item || array1Item < array2Item){
      mergedArray.push(array1Item);
      array1Item = array1[i];
      i++;
    } else {
      mergedArray.push(array2Item);
      array2Item = array2[j];
      j++;
    }
  }
  
  return mergedArray;

mergeSortedArray([0,3,4,31], [4,6,30]);
```

**python**

```python
# list.sort()
# sorted(list) -> retrun 
def mergeSortedArray(array1, array2):
  newArray = array1 + array2
  newArray.sort()

# 반복요소 제거 -> set
list(set(newArray))

# 문자열의 길이를 기준으로 정렬 key
list.sort(key = lambda x : len(x))
```

<br/>

<br/>

### pros

빠른 검색, 빠른 push과 pop, 순서(index) -> 메모리가 근처

### Conds

느린 삽입(insert), delete

고정된 사이즈(dynamic도 존재)