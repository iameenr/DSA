public class Main {
    public static void main(String[] args) {
        // Node root = null;
        int[] BSTValues = new int[]{30,5,1,7,12,33,43,2,9};
        Node root = new Node(BSTValues[0]);
        for(int x=1; x < BSTValues.length; x++) {
            root = root.insert(root, BSTValues[x]);
        }
        
        root.printInOrder(root);
        System.out.println("\n Closest In BST "+root.closestInBST(root, 10));
    }   
}

class Node{
    Node left, right;
    int value;
    Node(int value){
        this.value = value;
    }

    Node insert(Node root, int value){ 
        if(root == null) 
            return new Node(value);

        if(value <= root.value)
            root.left=insert(root.left, value);
        else
            root.right=insert(root.right, value);

        return root;
    }

    void printInOrder(Node root){ 
        if(root == null) return;

        printInOrder(root.left);
        System.out.print(root.value+", ");
        printInOrder(root.right);
    }

    int closestInBST(Node root, int target){ 
        int minDifference = target - root.value;
        while(true){ 
            // System.out.println("here..");
            if(root == null)
                return target - minDifference;
            
            if(Math.abs(target - root.value) <= Math.abs(minDifference))
                minDifference = target - root.value;
            else
                return target - minDifference;
                
            if(minDifference < 0){ root = root.left; }
            else if(minDifference > 0){ root = root.right; }
            else { return target; }
        }
    }
}
