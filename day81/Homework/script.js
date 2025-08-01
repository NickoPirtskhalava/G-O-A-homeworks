// 1)
for (let i = 2; i <= 20; i += 2) {
  console.log(i);
}

// 2)
let str = "Nicko";
for (let i = 0; i < str.length; i++) {
  console.log(str[i]);
}

// 3)
let arr = ["a", "b", "c", "d", "e", "f"];
for (let i = 0; i < arr.length; i++) {
  if (i % 2 === 0) {
    console.log(arr[i]);
  }
}

// 4)
let i = 1;
while (i <= 50) {
  if (i % 2 === 0) {
    console.log(i);
  }
  i++;
}

// 5)
let j = 1;
let sum = 0;
while (j <= 80) {
  if (j % 2 === 0) {
    sum += j;
  }
  j++;
}
console.log("Sum of even numbers:", sum);