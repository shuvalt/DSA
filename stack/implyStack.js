class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Stack{
    constructor(){
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }
    peek(){
        return this.top;
    }
    push(value){
        const newNode = new Node(value);
        if(this.length === 0){
            this.top = newNode;
            this.buttom = newNode;
        }else{
            const holdingNode = this.top;
            this.top = newNode;
            this.top.next = holdingNode;
        }
        this.length++;
        return this;
    }
    pop(){
        if(!this.top){
            return "stack is empty"
        }
        if(this.top === this.buttom){
            this.buttom = null;
        }
        this.top = this.top.next;
        this.length--;
        return this;
    }
}

const myStack = new  Stack();
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.pop()
console.log(myStack.peek());
