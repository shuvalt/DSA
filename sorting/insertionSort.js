function insertionSort(ar){
    l = ar.length;
    for(let i=1;i<l;i++){
        key = ar[i]
        j = i -1
        while(j>=0 && ar[j] > key){
            ar[j+1] = arr[j]
            j--
        }
        ar[j+1] = key
    }
    return ar
}

let arr = [8,1,6,2,5,4,6,7,3]

console.log(insertionSort(arr))
