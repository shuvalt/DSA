function bubbleSort(ar){
    l = ar.length;
    for(let i=0;i<l;i++){
        for(let j=i;j<l;j++){
            if(ar[j] > ar[j+1]){
                const t = ar[j]
                ar[j] = ar[j+1]
                ar[j+1] = t
            }
        }
    }
    return ar
}

let arr = [8,1,6,2,5,4,6,7,3]

console.log(bubbleSort(arr))
