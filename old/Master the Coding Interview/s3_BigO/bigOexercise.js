function funChallenge(input) {
  let a = 10; //O(1)
  a = 50 + 3; //O(1)

  for (let i = 0; i < input.length; i++) {
    //O(n), linear time
    anotherFunction(); //O(n) -> input에 달렸다
    let stranger = true; //O(n)
    a++; //O(n)
  }
  return a; //O(1)
}

funChallenge();

//BIG O(3 + 4n) = O(n)
