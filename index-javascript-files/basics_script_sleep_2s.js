

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
async function sleep_() {
    console.log("[basics_script_sleep_2s.js] Czekam 2 sekundy...");
    await sleep(2000); // Program tutaj "pauzuje"

    console.log("[basics_script_sleep_2s.js] Gotowe! Czekałem 2 sekundy.");
}

sleep_();
