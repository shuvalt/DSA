function selectionSort(ar){
    l = ar.length;
    for(let i=0;i<l;i++){
        let small = i;
        for(let j=i+1;j<l;j++){
            if(ar[small]>ar[j]){
                small = j
            }
        }
        const t = ar[i]
        ar[i] = ar[small]
        ar[small] = t
    }
    return ar
}

let arr = [8,1,6,2,5,4,6,7,3]

console.log(selectionSort(arr))
