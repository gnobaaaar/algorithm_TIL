## LOOP

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



