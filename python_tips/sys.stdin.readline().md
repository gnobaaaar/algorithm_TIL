## 💡 input()대신 sys.stdin.readline()을 사용하는 이유

한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 `input()`으로 입력 받는다면 시간초과가 발생할 수 있습니다. 대표적인 예시가 백준 BOJ 15552번 문제입니다.

<br />

<br />

## sys.stdin.readline() 사용법

```python
import sys

T = int(input())	#Test Case
for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)
```

<br />

### 한 개의 정수 입력 받을 때

```python
import sys
a = int(sys.stdin.readline())
```

한 줄 단위로 받기에 개행문자가 입력받아진다,

따라서 개행 문자를 제거해야한다.

<br />

### 정해진 개수의 정수를 한 줄에 입력받을 때

```python
import sys
a,b,c = map(int, sys.stdin.readline().split())
```

split()을 통해 문자열을 나누어준다.

`map()` 은 반복가능한객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해 준다

<br />

### 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때

```python
import sys
data = []
n = int(sys.stdin.readline())
for i in range(n):
  data.append(list(map(int, sys.stdin.readline().split())))
```

각 요소의 길이가 동일한, 다른 2차원 리스트로 만들 수 있다

<br />

### 문자열 n줄을 입력받아 리스트에 저장

```python
import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

`strip()` 은 문자열 맨 앞과 맨 끝의 공백문자를 제거한다

<br />

👉 입력

```null
3
안녕안녕
나는 지수야
헬륨가스 마셨더니 이렇게됐지
```

👉 출력
`['안녕안녕', '나는 지수야', '헬륨가스 마셨더니 이렇게됐지']`



> 출처
>
> [[Python 문법\] 파이썬 입력 받기(sys.stdin.readline) (velog.io)](https://velog.io/@yeseolee/Python-파이썬-입력-정리sys.stdin.readline)



