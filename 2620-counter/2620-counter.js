/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let i = n - 1
    
    return function() {
        i += 1
        return i
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */