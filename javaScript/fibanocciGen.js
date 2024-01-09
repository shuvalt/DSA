var fibGenerator = function*(start = 0, end = Infinity, step = 1) {
    let a = -1;
    let b = 1;
    for(let i = start; i < end; i += step){
        re = a+b;
        a = b;
        b = re;
        yield re;
    }
};
