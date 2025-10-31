
export function objectSize(obj) {
  const objectString = JSON.stringify(obj);
  return new TextEncoder().encode(objectString).length; // bajty UTF-8
}

function sleepSync(ms) {
  const start = Date.now();
  while (Date.now() - start < ms) {}
}

function a_sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

export async function f_sleep(seconds, funct=null, ...funct_params) {
  // console.log("Start");
  await a_sleep(seconds * 1000);
  console.log(`Logging this with ${seconds} seconds delay.`);

  if ( funct === null ) {
    // do nothing
  }
  else {
    if ( funct_params )  { funct(funct_params) }
    else { funct() }
  }

}

export function dir(obj, { includeNonEnumerable = false, includeSymbols = false, stopAtObjectPrototype = true } = {}) {
  if (obj === null || obj === undefined) return [];
  const names = new Set();

  let cur = obj;
  while (cur !== null) {
    if (includeNonEnumerable) {
      Reflect.ownKeys(cur).forEach(k => {
        if (typeof k === 'symbol' && !includeSymbols) return;
        names.add(String(k));
      });
    } else {
      // enumerable + symbols if requested
      Object.keys(cur).forEach(k => names.add(String(k)));
      if (includeSymbols) {
        Object.getOwnPropertySymbols(cur).forEach(s => names.add(String(s)));
      }
    }

    if (stopAtObjectPrototype && cur === Object.prototype) break;
    cur = Object.getPrototypeOf(cur);
  }

  return Array.from(names).sort();
}


export function prototypePresentation() {
    console.log("Starting/Logging prototypePresentation.");

    // 1
    const personProto = {
        greet() {
        console.log("[DEBUG] Cześć, jestem greet (prototypePresentation).");
        }
    }

    const user = Object.create(personProto); // ustawia personProto jako prototyp
    user.greet();
    user.name = "John";
    console.log("[DEBUG] Reflect.ownKeys(user): ", Reflect.ownKeys(user));
    console.log("[DEBUG] Object.keys(user): ", Object.keys(user));
    console.log("[DEBUG] Object.prototype: ", Object.prototype);
    console.log("[DEBUG] Object.getPrototypeOf({user}): ", Object.getPrototypeOf(user));

    // 2
    function Person(name) {
      this.name = name;
    }

    Person.prototype.greet = function() {
      console.log("Cześć, jestem " + this.name);
    };

    const user2 = new Person("Ala");
    user2.greet(); // "Cześć, jestem Ala"
    console.log(Object.getPrototypeOf(user2) === Person.prototype); // true

    // 3
    const proto = { sayHi() { console.log("Hi"); } };
    const obj = {};
    Object.setPrototypeOf(obj, proto);
    obj.sayHi(); // "Hi"

    // 4
    class XPerson {
      constructor(name) {
        this.name = name;
      }
      greet() {
        console.log("Cześć, jestem " + this.name);
      }
    }

    const xuser = new XPerson("Ola");
    xuser.greet(); // "Cześć, jestem Ola"
    console.log(Object.getPrototypeOf(xuser) === XPerson.prototype); // true


    console.log("\nEnding/Logging prototypePresentation.");
}

export function getRequest(url) {
    console.log("[DEBUG] Starting/Logging getRequest.");

    fetch(url, {
      method: 'GET', // opcjonalnie, bo GET jest domyślny
      headers: {
        // 'Content-Type': 'application/plain',
        // 'X-Custom-Header': 'MojaWlasnaWartosc'
      }
    })
    .then(response => response.text())
    .then(data => console.log('Otrzymane dane:\n - ', data))
    .catch(error => console.error('Błąd:', error));

    console.log("[DEBUG] Ending/Logging getRequest.");
}
