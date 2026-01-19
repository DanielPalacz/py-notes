
// 1. if - else if - else

if (window.x == 101) {
    console.log("Tak, window.x = 101.");
} else if  (window.x == 102) {
    console.log("Tak, window.x = 102.");
} else {
    console.log("Nie, window.x != 101.");
}


// 2. for ... of
//
//ABC = 1;
//
//for (const elem of Object.keys(globalThis)) {
//    console.log("[basics_script1a.js] -", elem, "-", globalThis[elem]);
//}


// 3. for ... in

const obj = { a: 11, b: 12, c: 13 };

for (const property in obj) {
  console.log(`[basics_script1a.js] - ${property}: ${obj[property]}`);
}
