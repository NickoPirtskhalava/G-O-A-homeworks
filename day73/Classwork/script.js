// Step 1: Create two separate lists
let numbers = [1,2,3,4,5,6,7,8,9,10];
let strings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];

let combined = numbers.concat(strings);

delete combined[5];

combined.pop();

combined.shift();

combined.splice(1, 0, "ვანო");

combined.push("მოთიაშვილი");

let result = combined.join(", ");

console.log(result);