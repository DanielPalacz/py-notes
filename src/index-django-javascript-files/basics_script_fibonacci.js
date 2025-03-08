let a = 0;
let b = 1;

function runFibonacci(num) {
  while (a < num) {
    console.log(a); // Wypisuje bieżącą wartość `a`
    let temp = a; // Zapisujemy wartość `a` do zmiennej pomocniczej
    a = b; // Przypisujemy `b` do `a` (przechodzimy na następną liczbę)
    b = temp + b; // Przypisujemy sumę poprzednich dwóch liczb do `b`
  }
  console.log('Checking this object in global function. This is:', this);
}

let x = runFibonacci(200);
console.log("runFibonacci returned:", x);
console.log('Checking this object in global context. This is:', this);
