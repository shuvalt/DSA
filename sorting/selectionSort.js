function selectionSort(ar){
    l = ar.length;
    for(let i=0;i<l;i++){
        let small = i;
        for(let j=i;j<l;j++){
            if(ar[small]>ar[j+1]){
                small = j+1
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
