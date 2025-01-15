function generateRandomNumber() {
  let randomNumber = Math.floor(Math.random() * 100);
  console.log(`JavaScript z zewnętrznego pliku 2 [${Date.now()}][${randomNumber}]`);
}

generateRandomNumber();
