# 2차원 배열 선언

> **2중 for문으로 2중 리스트 선언**

```
array = [[0 for col in range(11)] for row in range(10)]
```

11x10 리스트를 생성합니다. = (11열 10행)

 

> ***연산자와 for문으로 리스트 선언**

```
array = [[0]*11 for i in range(10)]
```