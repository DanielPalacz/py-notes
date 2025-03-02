function generateRandomNumber() {
  let randomNumber = Math.floor(Math.random() * 100);
  console.log(`JavaScript z zewnętrznego pliku 2 [${Date.now()}][${randomNumber}]`);
  document.addEventListener("DOMContentLoaded", function () {
    document.body.innerHTML += `<p>[JS script external file] H! Random number is: ${randomNumber}</p>`;
  });
}

generateRandomNumber();
