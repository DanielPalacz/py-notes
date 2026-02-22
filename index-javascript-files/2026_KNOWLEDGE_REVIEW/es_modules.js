
export function generateRandomNumber() {
  let randomNumber = Math.floor(Math.random() * 100);

  console.log(`[DEBUG][LOG][generateRandomNumber] Generating random number, randomNumber=${randomNumber}.`);
  document.addEventListener("DOMContentLoaded", function () {
    document.body.innerHTML += `<p>[ES6 module import][generateRandomNumber] Hi, generated random number it is: ${randomNumber}.</p>`;
  });
}
