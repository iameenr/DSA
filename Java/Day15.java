import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;
    Node(int d) {
        data = d;
        next = null;
    }
}

public class Day15 {

    public static  Node insert(Node head,int data) {
        Node nextnode = new Node(data);
        nextnode.next = null;
        if(head == null)
            head = nextnode;
        else{
            Node traversal_helper;
            traversal_helper = head;
            while(traversal_helper.next != null)
                traversal_helper = traversal_helper.next;

            traversal_helper.next = nextnode;
        }
        return head;
    }

    public static void display(Node head) {
        Node start = head;
        while(start != null) {
            System.out.print(start.data + " ");
            start = start.next;
        }
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Node head = null;
        int N = sc.nextInt();

        while(N-- > 0) {
            int ele = sc.nextInt();
            head = insert(head,ele);
        }
        display(head);
        sc.close();
    }
}