export function generateRandomNumber() {
  let x = 101; // 'let', 'const', 'var' - no? then x goes to global;

  let randomNumber = Math.floor(Math.random() * 100);
  console.log(`[DEBUG][ES6 ECMA module] JavaScript z zewnętrznego pliku 2 [${Date.now()}][randomNumber=${randomNumber}]`);
  document.addEventListener("DOMContentLoaded", function () {
    document.body.innerHTML += `<p>[JS script external file] H! Random number is: ${randomNumber}</p>`;
  });
}
