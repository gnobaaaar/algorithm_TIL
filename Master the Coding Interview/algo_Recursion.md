# Recursion

๐ : DRY, Readability

๐ฑ : Large Stack

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

๋ถํ  ์ ๋ณต๋ฒ์ ์ฌ๊ท์ ์ผ๋ก ์์ ์ ํธ์ถํ๋ฉด์ ๊ทธ ์ฐ์ฐ์ ๋จ์๋ฅผ ์กฐ๊ธ์ฉ ์ค์ด๊ฐ๋ ๋ฐฉ์

```
function F(x):
  if F(x)๊ฐ ๊ฐ๋จ then:
    return F(x)๋ฅผ ๊ณ์ฐํ ๊ฐ
  else:
    x ๋ฅผ x1, x2๋ก ๋ถํ 
    F(x1)๊ณผ F(x2)๋ฅผ ํธ์ถ
    return F(x1), F(x2)๋ก F(x)๋ฅผ ๊ตฌํ ๊ฐ
```

1. ๋ถํ  : ์๋ ๋ฌธ์ ๋ฅผ ๋ถํ ํ์ฌ ๋ ํ์์ ๋ฌธ์ ๋ก ๋๋๋ค
2. ์ ๋ณต : ํ์ ๋ฌธ์  ๊ฐ๊ฐ์ ์ฌ๊ท์ ์ผ๋ก ํด๊ฒฐํ๋ค(๋์ด์ ๋ถํ ๋์ง ์๊ณ  ํด๊ฒฐ๋๋ ๋ฌธ์  -> base case)
3. ๋ณํฉ : ํ์๋ฌธ์ ๋ค์ ๋ต์ ํฉ์ณ์ ์๋์ ๋ฌธ์ ๋ฅผ ํด๊ฒฐ

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

