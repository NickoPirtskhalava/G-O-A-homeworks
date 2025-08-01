// 1)
let list = [];
for (let i = 0; i < 30; i++) {
  list.push(i + 1);
}
for (let item of list) {
  console.log(item);
}

// 2)
let list1 = [];
let list2 = [];
for (let i = 0; i < 10; i++) {
  list1.push(i + 1);
}
for (let item of list1) {
  list2.push(item);
}
console.log(list2);

// 3)
let text = "Hello World";
let vowels = "aeiouAEIOU";
for (let char of text) {
  if (vowels.includes(char)) {
    console.log(char);
  }
}

// 4)
// block scope: ცვლადი ხელმისაწვდომია მხოლოდ ბლოკის შიგნით { }
// global scope: ცვლადი ხელმისაწვდომია მთელ სკრიპტში
// local scope: ცვლადი ხელმისაწვდომია მხოლოდ ფუნქციის შიგნით

// 5)
// global scope
let globalVar = "I'm global";

function showGlobal() {
  console.log(globalVar);
}
showGlobal();

// local scope
function localExample() {
  let localVar = "I'm local";
  console.log(localVar);
}
localExample();

// block scope
if (true) {
  let blockVar = "I'm block scoped";
  console.log(blockVar);
}