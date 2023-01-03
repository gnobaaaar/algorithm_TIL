# Recursion

😃 : DRY, Readability

😱 : Large Stack

Data Structure + Algorithms = Programs

common topic of interview

**refer to itself**

stack overflow

merge sort. quick sort, tree/graph traversal

<br/>

### Anatomy of Recursion

```javascript
let counter = 0;
function inception(){
  //console.log(counter)
  if(counter > 3){
    return 'done!';		// why no done? -> debugger;
   }
  counter++;
  //inception(); -> no return -> local variable is disappear
  return inception();
}

// inception(inception(inception('done';);););
inception();
```

1. Identify the base **case**
2. Identify the recursive **case**
3. Get closer and closer and **return**

when needed. Usually you have 2 returns

<br/>

### Factorial Exercise

```javascript
function findFactorialRecursion(number){		//O(n)
  //code here
  if (number === 2){
    return 2;
  }
  answer = number * (findFactorialRecursion(number-1));
  return answer;
}

function findFactorialIterative(number){		//O(n)
  //code here
  let answer = 1;
  if (number === 2){
    answer = 2;
  }
  for(let i=2; i < number+1; i++){
    answer = answer * i;
  }
  return answer;
}
```

<br/>

### Fibonacci

```javascript
function fibonacciIterative(n){		// O(n-2) = O(n)
  let arr = [0,1];
  for (let i=2; i<n+1; i++){
    arr.push(arr[i-2]+arr[i-1]);
  }
  return arr[n];
}
fibonacciIterative(3);

function fibonacciRecursive(n){		// O(2^N) -> pretty bad 
  if (n < 2){
    return n;
  }
  return fibonacciRecursive(n-1) + fibonacciRecursive(n-2);
}
fibonacciRecursive(3);
```

<br/>

### Divide and Conquer using Recursion

분할 정복법은 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄어가는 방식

```
function F(x):
  if F(x)가 간단 then:
    return F(x)를 계산한 값
  else:
    x 를 x1, x2로 분할
    F(x1)과 F(x2)를 호출
    return F(x1), F(x2)로 F(x)를 구한 값
```

1. 분할 : 원래 문제를 분할하여 더 하위의 문제로 나눈다
2. 정복 : 하위 문제 각각을 재귀적으로 해결한다(더이상 분할되지 않고 해결되는 문제 -> base case)
3. 병합 : 하위문제들의 답을 합쳐서 원래의 문제를 해결

<br/>

### reverseString

```javascript
function reverseString(str){
  let arrayStr = str.split('');
  let reverseArray = [];
  
  function addToArray(array){
    if(array.length > 0){
      reverseArray.push(array.pop());
      addToArray(array);
    }
    return;
  }
  addToArray(arrayStr);
  return reverseArray.join('');
}

function reverseStringRecursvie(str){
  if(str === ''){
    return "";
  }else{
    return reverseStringRecursvie(str.substr(1)) + str.charAt(0);
  }
}

reverseString('yoyo master');
reverseStringRecursvie('yoyo master');
```

<br/>

