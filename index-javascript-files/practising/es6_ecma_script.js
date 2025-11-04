export function generateRandomNumber() {
  let x = 101; // 'let', 'const', 'var' - no? then x goes to global;

  let randomNumber = Math.floor(Math.random() * 100);
  console.log(`[DEBUG 7][ES6 ECMA module] executing ECMA style exported function [${Date.now()}][randomNumber=${randomNumber}]`);
  document.addEventListener("DOMContentLoaded", function () {
    document.body.innerHTML += `<p>[JS script external file] Hi. Random number is: ${randomNumber}</p>`;
  });

}
