class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class Queue{
    constructor(){
        this.first = null;
        this.last = null;
        this.length = 0;
    }
    peek(){
        return this.first;
    }
    enQueue(value){
        const newNode = new Node(value);
        if(this.length === 0){
            this.first = newNode;
            this.last = newNode;
        }else{
            this.last.next = newNode;
            this.last = newNode;
        }
        this.length++;
        return this;
    }
    deQueue(){
        if(!this.first){
            return "empty queue"
        }
        if(this.last == this.first){
            this.last = null;
        }
        this.first = this.first.next;
        this.length--;
        
    }
}
