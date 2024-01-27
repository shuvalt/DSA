class Node{
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class binarySearchTree{
    constructor(){
        this.root = null;
    }

    //inserting
    insert(value){
        const newNode = new Node(value);
        if(this.root === null){
            this.root = newNode;
        }else{
            let currentNode = this.root;
            while(true){
                if(value<currentNode){
                    if(!currentNode.left){
                        currentNode.left = newNode;
                        return this;
                    }
                    currentNode = currentNode.left;
                }
                else{
                    if(!currentNode.right){
                        currentNode.right = newNode;
                        return this;
                    }
                    currentNode = currentNode.right
                }
            }
        }
    }
}
