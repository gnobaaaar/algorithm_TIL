## BIG O'S RULES

1. **Worst Case in Senario**
2. **Remove Constants**
3. **Different terms for inputs** 

```java
function compressBoxesTwice(boxes, boxes2){		//Different inputs
  boxes.forEach(function(boxes){
    console.log(boxes);
  })
  boxes2.forEach(function(boxes){
    console.log(boxes);
  })  
}

//O(2n=n) X
//O(a + b) O -> we don't know
//if nested ->O(a*b)
```

4. **Drop Non Dominants**

<br/>

<br/>

## BIG O'S

`O(1)` Constant - no loops

`O(log N)` Logarithmic - usually searching algorithms have log n if they are sorted (**Binary Search**)

`O(n)` Linear - for loops, while loops through n items

`O(n log(n))` Log Linear - **usually sorting operations**

`O(n^2)` Quadratic - every element in a collection needs to be compared to ever other element. Two nested loops

`O(2^n)` Exponential - **recursive algorithms** that solves a problem of size N

`O(n!)` Factorial - you are adding a loop for every element

**Iterating through half a collection is still `O(n)`**

**Two separate collections: `O(a \* b)`**

<br/>

<br/>

## WHAT CAN CAUSE TIME IN A FUNCTION?

- Operations (`+`,`-`, `\*`, `/`)
- Comparisons (`<`, `>`, `===`)
- Looping (`for`, `while`)
- Outside Function call (`function()`)

<br/><br/>

## RULE BOOK

**Rule 1:** Always worst Case

**Rule 2:** Remove Constants

**Rule 3:**

- Different inputs should have different variables: `O(a + b)`.
- A and B arrays nested would be: `O(a * b)`

\+ for steps in order

\* for nested steps

**Rule 4:** Drop Non-dominant terms

<br/><br/>

## WHAT CAUSES SPACE COMPLEXITY?

- **Variables**
- **Data Structures**
- **Function Call**
- **Allocations**





![Understanding time complexity with Python examples | by Kelvin Salton do  Prado | Towards Data Science](image/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)
