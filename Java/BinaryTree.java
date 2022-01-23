import java.util.HashMap;
import java.util.Map;

import javafx.util.Pair;

class Node {    
    int value; 
    Node left, right; 
        
    Node(int value){ 
        this.value = value; 
        left = null; 
        right = null; 
    } 
} 

class Tree {  
    Node root;
    Tree(int value){ 
        this.root = new Node(value);
    }


    void insert(int value){ 
        insertHelper(this.root, value);
    }
    void insertHelper(Node node, int value) {
        if (value < node.value) { 
            if (node.left != null) { insertHelper(node.left, value); } else { System.out.println(" Inserted " + value + " to left of " + node.value); node.left = new Node(value); } } else if (value > node.value) {
          if (node.right != null) {
            insertHelper(node.right, value);
          } else {
            System.out.println("  Inserted " + value + " to right of "
                + node.value);
            node.right = new Node(value);
          }
        }
      }

    void traverseInOrder(Node node) {
        if (node != null) {
            traverseInOrder(node.left);
            System.out.print(" " + node.value);
            traverseInOrder(node.right);
        }
    }

    int height(){
        return heightReccursion(root);
    }
    
    int height(Node node){
        return heightReccursion(node);
    }

    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    int heightReccursion(Node node){ 
        
        if(node == null) return 0;
        if(map.containsKey(node.value))
            return map.get(node.value);
        else
            map.put(node.value, Math.max(1 + heightReccursion(node.left), 1 + heightReccursion(node.right)));
        return map.get(node.value);
    }

    int diameter(){
        return diameterReccursion(root);
    }

    int diameterReccursion(Node node){
        if(node == null) return 0;
        
        int dthis, dl, dr;
        dthis = height(node.left) + height(node.right) + 2;
        dl = diameterReccursion(node.left);
        dr = diameterReccursion(node.right);

        if(dthis >= dl && dthis >= dr) return dthis;
        else if(dl >= dthis && dl >= dr) return dl;
        else return dr;
    }

    // boolean isHeightBalancedHelper(Node node){
    //     //base case
    //     if(node == null) return true;

    //     isHeightBalancedHelper(node.left);
    //     isHeightBalancedHelper(node.right);

    //     return (Math.abs(height(node.left) - height(node.right)) <= 1);
    // }

   class Pair{
        int height;
        boolean balanced;

        Pair(int height, boolean balanced){
            this.height = height;
            this.balanced = balanced;
        }

        Pair(){}
    }
    
     boolean isHeightBalanced(){
        Pair result = new Pair();
        result = isHeightBalancedHelper(root);
        return result.balanced;               
    }

    Pair isHeightBalancedHelper(Node node){
        //base case
        Pair p = new Pair();
        Pair left = new Pair();
        Pair right = new Pair();

        if(node == null){ 
            return new Pair(0,true);
        };

        left = isHeightBalancedHelper(node.left);
        right = isHeightBalancedHelper(node.right);
        p.height = Math.max(left.height, right.height) + 1;

        if(Math.abs(left.height - right.height) <= 1 && left.balanced && right.balanced)
            return new Pair(p.height, true);

        return new Pair(p.height, false);        
    }
}

public class BinaryTree{
    public static void main(String args[]){ 
        Tree tree = new Tree(5);
        System.out.println("Binary Tree Example");
        int[] treeList = new int[]{1,3,6,7,4,9,11,12,13,14};
        for(int i : treeList)
            tree.insert(i);
        
        System.out.println("Height: "+ tree.height()); 
        System.out.println("Diameter: "+ tree.diameter());

        if(tree.isHeightBalanced())
            System.out.println("HB"); 
        else
            System.out.println("not HB"); 

        
        
        }

}