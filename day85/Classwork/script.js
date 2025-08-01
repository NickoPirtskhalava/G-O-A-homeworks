// 1)
let arr = [1, 2, 3, 4];
for (let item of arr) {
  console.log(item);
}

// 2)
let str = "Nicko";
for (let char of str) {
  console.log(char);
}

// 3)
let obj = {name: "Nicko", age: 17};
for (let key in obj) {
  console.log(key, obj[key]);
}

// 4)
let globalVar = "I'm global";

function testScope() {
let localVar = "I'm local";

  if (true) {
    let blockVar = "I'm block scoped";
    console.log(blockVar);
  }

  console.log(localVar);
}

console.log(globalVar);
testScope();