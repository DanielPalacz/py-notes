
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

let x = runFibonacci(6);

console.log("runFibonacci returned:", x);
console.log('Checking this object in global context. This is:', this);
