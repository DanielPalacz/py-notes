function generateRandomNumber() {
    const currentScript = document.currentScript;
    if (currentScript.defer) {
      currentScriptMode = 'defer';
    } else if (currentScript.async) {
      currentScriptMode = 'async';
    } else {
      currentScriptMode = 'blocking';
    }

  x = 101; // 'let', 'const', 'var' - no? then x goes to global;

  let randomNumber = Math.floor(Math.random() * 100);
  console.log(`[DEBUG][basics_script.js][${currentScriptMode} mode][generateRandomNumber] Running JavaScript script by loading external JS file - [${Date.now()}][randomNumber=${randomNumber}]`);
  document.addEventListener("DOMContentLoaded", function () {
    document.body.innerHTML += `<p>[JS script external file] H! Random number is: ${randomNumber}</p>`;
  });
}

generateRandomNumber();
