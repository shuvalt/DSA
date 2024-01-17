let str = new String(33)
str = "hello world, how are you?"
let space = 0;
for(let i=0;i<str.length;i++){
    if(str[i]===" "){
        space++;
    }
}
idx = str.length + 2*space;
for(let i=str.length - 1;i>=0;i--){
    if(str[i]===" "){
        str[idx-1]="0"
        str[idx-2]="2"
        str[idx-3]="%"
        idx-=3
    }
    else{
        str[idx-1] = str[i]
        idx--;
    }
}
console.log(str)
