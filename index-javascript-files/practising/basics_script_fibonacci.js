

function runFibonacci(num) {
  let a = 0;
  let b = 1;
  while (a < num) {
    let temp = a; // Zapisujemy wartość `a` do zmiennej pomocniczej
    a = b; // Przypisujemy `b` do `a` (przechodzimy na następną liczbę)
    b = temp + b; // Przypisujemy sumę poprzednich dwóch liczb do `b`
  }
  // console.log('Checking this object in global function. This is:', this);
  return b
}

console.log("[DEBUG][basics_script_fibonacci.js][runFibonacci] triggering runFibonacci(6) function execution.");
let x2 = runFibonacci(6);

//console.log("[DEBUG][basics_script_fibonacci.js][runFibonacci] runFibonacci(6) returned:", x);
