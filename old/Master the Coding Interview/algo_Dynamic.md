# Dynamic Algorithms

### Memorization - Caching

**DYNAMIC PRGRAMMING is.. an** **optimization technique.**
**dynamic programming =** **divide and conquer + memoization**

<br/>

언제 Dynamic Programming을 적용할지에 대한 Cheatsheet

> 1. Can be divided into subproblem?
> 2. Recursive Solution
> 3. Are ther repetitive subproblems?
> 4. Memoize subproblems
> 5. Demand a raise from your boss

<br/>

피보나치 수열 -> 동적프로그래밍

```javascript
function fibonacciMaster() { // O(n)
  let cache = {};
  return function fib(n) {
    if (n in cache) return cache[n];
    else {
      if (n < 2) return n;
      cache[n] = fib(n-1) + fib(n-2);
      return cache[n];
    }
  }
}
```

Memoization을 활용하는 알고리즘 문제들이다.

☞ [House Robber](https://leetcode.com/problems/house-robber/)

☞ [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

☞ [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

<br/>

