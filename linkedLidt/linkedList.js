class Node{
    constructor(value){
        this.value = value,
        this.next = null
    }
}
class linkedList{
    constructor(value){
        this.head = {
           value : value,
           next : null
        }  
        this.tail = this.head;
        this.length = 1;
    }
    append(value){
        const newNode = new Node(value)
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }
    prepend(value){
        const newNode = new Node(value)
        newNode.next = this.head
        this.head = newNode; 
        this.length++;
        return this;
    }
    printList(){
        const array = [];
        let currentNode = this.head;
        while(currentNode !== null){
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
    insert(index,value){
        const newNode = new Node(value);
        if(index>this.length){
            this.length++;
            return this.append(value);
        }
        const leading = this.traverseToIndex(index-1);
        const folow = leading.next;
        leading.next = newNode;
        newNode.next = folow;
        this.length++;
    }
    remove(index){
        const toRemove = this.traverseToIndex(index-1);
        toRemove.next = toRemove.next.next;
        this.length--;
    }
    traverseToIndex(index){
        let counter = 0;
        let currentNode = this.head;
        while(counter != index){
            currentNode = currentNode.next;
            counter++;
        }
        return currentNode;
    }
}




const myLinkedList = new linkedList(5);
myLinkedList.append(10)
myLinkedList.append(16)
myLinkedList.prepend(19)
myLinkedList.insert(10,90)
myLinkedList.remove(2)

console.log(myLinkedList.printList())
