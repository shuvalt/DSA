function findRecurr(arr){
    let s =new Set();
    for(let i =0;i<arr.length;i++){
        if(!s.has(arr[i])){
            s.add(arr[i]);
        }
        else{
            return arr[i];
        }
    }
    return undefined;
}

console.log(findRecurr([2,5,1,3,4,5]))
console.log(findRecurr([2,1,1,2,3,5,1,2,4]))
console.log(findRecurr([2,3,4,5]))
