var chunk = function(arr, size) {
    let re = [];
    let lora; //length of result array
    let l = 0;
    n = arr.length;
    lora = Math.ceil(n / size);
    for(let i = 0; i<lora;i++){
        let ind = 0;
        temp = re[i]=[];
        while(ind<size){
            if(l==n){
                return re
            }
            temp.push(arr[l]);
            ind++;
            l++;
            }
    }
    return re;
};
