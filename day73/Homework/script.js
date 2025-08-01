// // 1)
// concat() — აერთიანებს ორ ან მეტ სიას ახალ სიაში
// delete — შლის ელემენტს, მაგრამ ტოვებს undefined
// pop() — შლის ბოლო ელემენტს სიიდან
// shift() — შლის პირველ ელემენტს სიიდან
// splice() — შლის ან ამატებს ელემენტებს კონკრეტულ ინდექსზე
// push() — ამატებს ელემენტს ბოლოში
// join() — აერთიანებს სიას სტრინგად

// // 3)
let numbers = [1,2,3,4,5,6,7,8,9,10];
let strings = ["a","b","c","d","e","f","g","h","i","j"];

let combined = numbers.concat(strings);

delete combined[5];

combined.pop()

combined.splice(1, 0, "ვანო");

combined.push("მოთიაშვილი");

let result = combined.join(", ");
console.log(result);

// // 4)
let list1 = [1, 2, 3];
let list2 = ["a", "b", "c"];
let list3 = [true, false, null];

let merged1 = list1.concat(list2);

let merged2 = merged1.concat(list3);

merged2.splice(2, 4);

delete merged2[2];

console.log(merged2[merged2.length - 1]);