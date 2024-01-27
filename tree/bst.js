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

    lookUp(value){
        if(!this.root){
            return "tree is empty."
        }
        let currentNode = this.root;
        while(currentNode){
            if(value < currentNode.value){
                currentNode = currentNode.left;
            }else if(value > currentNode.value){
                currentNode = currentNode.right;
            }else if(value === currentNode.value){
                return currentNode.value;
            }
        }
    }
}
