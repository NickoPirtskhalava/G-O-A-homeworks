// 1. ახსნა DOM-ზე
console.log("DOM გვაძლევს საშუალებას ვმართოთ ვებსაიტის სტრუქტურა პროგრამულად.");

// 2. let vs const
let name = "Nicko";       // შესაძლოა შეიცვალოს
const birthYear = 2005;   // უცვლელი მნიშვნელობა

// 3. ღილაკი და alert
let button = document.createElement("button");
button.innerText = "Click Me";
button.onclick = function() {
  alert("Hello User");
};
document.body.appendChild(button);

// 4. img ზომის ცვლილება
let img = document.createElement("img");
img.src = "https://via.placeholder.com/100";
img.style.width = "100px";
img.onclick = function() {
  img.style.width = "300px";
};
document.body.appendChild(img);

// 5. ცვლადი და მნიშვნელობა
let mood = "Ready for success!";
console.log(mood);

// 6. კოდის ანალიზი
let x = 5;
console.log(x++);  // ბეჭდავს 5-ს, შემდეგ x ხდება 6
console.log(++x);  // x ხდება 7 და ბეჭდავს 7-ს