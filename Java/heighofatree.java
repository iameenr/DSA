import java.util.HashMap;
import java.util.Map;

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
        if (value <= node.value) { 
            if (node.left != null) { insertHelper(node.left, value); } 
                else { System.out.println(" Inserted " + value + " to left of " + node.value); 
                node.left = new Node(value); 
            } 
        } 
        else if (value > node.value) {
            if (node.right != null) { insertHelper(node.right, value);}
                else { System.out.println("  Inserted " + value + " to right of "+ node.value);
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

    Map<Node, Integer> map = new HashMap<Node, Integer>();
    int heightReccursion(Node node){ 
        
        if(node == null) return 0;
        if(map.containsKey(node))
            return map.get(node);
        else
            map.put(node, Math.max(1 + heightReccursion(node.left), 1 + heightReccursion(node.right)));
        return map.get(node);
    }
}

public class heightofatree{
    public static void main(String args[]){ 
        Tree tree = new Tree(5);
        System.out.println("Binary Tree Example");
        int[] treeList = new int[]{1,3,6,7,4,9,11,12,13,14};
        for(int i : treeList)
            tree.insert(i);
        
        System.out.println("Height: "+ tree.height());         
    }
}