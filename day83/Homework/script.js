// 1)
function greetUser(number) {
  let i = 0;
  while (i < number) {
    console.log("Hello!");
    i++;
  }
}
greetUser(5);

// 2)
let num = 7;
let guess;
do {
  guess = parseInt(prompt("Enter a number between 1 and 10:"));
  switch (guess) {
    case num:
      alert("Correct! Welcome!");
      break;
    default:
      alert("Wrong number, try again.");
  }
} while (guess !== num);

// 3)
function checkDiscount(age) {
  if (age <= 19) {
    console.log("თქვენ მიიღეთ 30% ფასდაკლება");
  } else if (age >= 19 && age < 50) {
    console.log("თქვენ მიიღეთ 10% ფასდაკლება");
  } else {
    console.log("თქვენ მიიღეთ 50% ფასდაკლება");
  }
}
checkDiscount(25);

// 4)
for (let i = 0; i < 3; i++) {
  console.log("For loop:", i);
}

let j = 0;
while (j < 3) {
  console.log("While loop:", j);
  j++;
}

let color = "blue";
switch (color) {
  case "red":
    console.log("You chose red");
    break;
  case "blue":
    console.log("You chose blue");
    break;
  default:
    console.log("Unknown color");
}