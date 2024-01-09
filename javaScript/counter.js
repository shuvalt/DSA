var createCounter = function(init) {
    n = init
    re = {
        "increment":()=>{
            return ++n;
        },
        "decrement":()=>{
            return --n;
        },
        "reset":()=>{
            n = init;
            return n;
        }
    }
    return re;
};
