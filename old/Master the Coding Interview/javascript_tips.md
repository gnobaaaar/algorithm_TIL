### LOOP 3 ways

```javascript
function findNemo (array){
  for (let i =0 ; i< array.length; i++){
    if(i==='NEMO'){
      console.log('FOUND NEMO!')
    }
  }
}

const findNemo2 = array =>{
  array.forEach(fish =>{
    if(fish==='NEMO'){
      console.log('FOUND NEMO!')
    }
  })
}

const findNemo3 = array => {
  for (let fish of array){
    if(fish === 'NEMO'){
      console.log('FOUND NEMO!')
    }
  }
}
```

<br/>

### How Does Javscript Work?

![img](image/1*RLbK8nM3pfLWPu4qIUaWww-20220213160626569.png)

- Program
  - allocate memory
  - parse and excute

V8 engine

- memory heap : `const a = 1`

  - 메모리 할당을 담당하는 곳
  - 전역변수의 경우 사용되지 않으면 memory heap을 계속해서 채운다

- call stack

  - 코드가 호출되면서 스택으로 쌓이는 곳
  - 첫 줄을 읽고 콜스택에 넣어 실행하면서 제거한다

  ```javascript
  console.log('1');
  console.log('2');
  console.log('3');
  
  const one = () => {
    const two = () => {
      console.log('4');
    }
    two();
  }
  
  //스택에 one -> two 순으로 쌓인다 -> console.log('4')
  ```

싱글 스레드 = one call stack = 한 번에 하나의 작업만이 가능하다

<img src="https://miro.medium.com/max/1400/1*FA9NGxNB6-v1oI2qGEtlRQ.png" alt="img" style="zoom:67%;" />

- Event Loop
  - 이벤트 발생 시 호출되는 콜백 함수들을 테스트 큐에 전달, 태스크 큐의 콜백 함수들을 콜스택에 전달
- Task Queue
  - web api에서 비동기 작업들이 실행된 후 호출되는 콜백함수들이 기다리는 공간
  - FIFO
  - 태스크 큐는 여러개의 큐로 구성(Microtask Queue, Animation Frames)
- Web API
  - 브라우저에서 자체적으로 지원하는 api
  - DOM, Ajax(XmlHttpRequest), setTimeout 등의 비동기 작업을 지원
- **동시성을 보장하는 비동기, 논블록킹 작업들은 런타임 환경에서 담당(브라우저, Node.js)**

즉 setTimeout과 같은 콜백함수는 바로 콜스택이 아닌 web api에서 비동기 처리된 후 콜백함수가 태스크 큐로 전달

<br/>

