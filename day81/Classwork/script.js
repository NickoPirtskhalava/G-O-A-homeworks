// 1)
let num = parseInt(prompt("Enter a number:"));
let i = 0;
while (i <= num) {
  console.log(i);
  i++;
}

// 2)
let name = prompt("Enter your name:");
while (name.length < 10) {
  name = prompt("Name too short. Enter again:");
}

// 3)
let pin = prompt("Enter PIN:");
while (pin !== "6446") {
  pin = prompt("Wrong PIN. Try again:");
}

// 4)
let password = prompt("Enter password:");
while (password !== "ვანოჩკა") {
  password = prompt("Incorrect. Try again:");
}