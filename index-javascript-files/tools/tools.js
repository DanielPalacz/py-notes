window.dir_ = function(obj) {
    const props = new Set();
    let current = obj;
    while (current) {
        Object.getOwnPropertyNames(current).forEach(p => props.add(p));
        current = Object.getPrototypeOf(current);
    }
    return Array.from(props).sort();
};
console.log("dir_() loaded");