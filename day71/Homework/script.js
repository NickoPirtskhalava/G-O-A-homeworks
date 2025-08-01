// 1
console.log("nicko".toUpperCase());
console.log("hello".toUpperCase());


console.log("JAVASCRIPT".toLowerCase());
console.log("WORLD".toLowerCase());


console.log(Math.random());
console.log(Math.random());


console.log(Math.floor(4.9));
console.log(Math.floor(9.99));


console.log(Math.ceil(2.1));
console.log(Math.ceil(7.01));


console.log(Math.round(3.4));
console.log(Math.round(6.7));


console.log(Math.max(2, 9, 4));
console.log(Math.max(10, 1, 7));


console.log(Math.min(3, 0, -7));
console.log(Math.min(10, 20, 5));


// 2
// scope არის ცვლადების ხილვადობის არე
// Global scope
// Block scope
// Function scope

// 3
console.log(Math.floor(Math.random() * 100));

// 4
let rand = Math.ceil(Math.random() * 5);
console.log(Math.pow(rand, 2));

// 5
let person = {
  name: "Nicko",
  surname: "Kvaratskhelia",
  age: Math.floor(Math.random() * 20)
};
console.log(person);