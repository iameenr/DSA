// import java.util.*;

// class Graph{
//         ArrayList<ArrayList<Integers>> adjList;
//         boolean undirected;

//         Graph(int v, boolean undirected) {
//             this.undirected = undirected;
//             adjList = new ArrayList<ArrayList<Integers>>(5);

//             for (int i = 0; i < adjList.size(); i++) {
//                 adjList.get(i) = new ArrayList<Integers>();
//             }
//         }

//         void addEdge(int a, int b){
//             adjList.get(a).add(b);
//             if(this.undirected){
//                 adjList.get(b).add(a);
//             }
//         }

//         void printList(){
//             for (int i = 0; i < adjList.size(); i++) {
//                 System.out.println(adjList.get(i)+" ---> ");

//                 for (int j = 0; j < adjList.get(i).size(); j++) {
//                     System.out.print(adjList.get(i).get(j)+", ");    
//                 }
//                 System.out.println("");
//             }
//         }

//         void BFSTraversal(int source){
//             //Visited arrays a
//             boolean visited[v];
//             Queue<Integers>  q = new LinkedList<Integers>();
//             q.add(source);
//             visited[source] = true;

//             while(!q.isEmpty()){
//                 int vertex = q.remove();

//                 System.out.print("\n"+vertex+" -> ");

//                 for (int i = 0; i < q.get(vertex).size(); i++) {
//                     int nodeNow = adjList.get(vertex).get(i);
//                     if(!visited[nodeNow]){
//                         q.add(nodeNow);
//                         visited[nodeNow] = true;
//                 }
//             }
//         }
//     }

//     void DFSTraversalRecursion(int node, boolean visited[]){
//         visited[node] = true;
//         System.out.println(node+" -> ");

//         while(!visited[node]){
//             for(int i=0; i< adjList.get(node).size(); i++){  // for (int nbr : adjList.get(node)) DOES THIS WORK?  
//                 int neighbour = adjList.get(node).get(i);
//                 DFSTraversalRecursion(neighbour, visited)
//             }
//         }
//     }

//     void DFSTraversal(int source){
//         boolean visited[v];
//         DFSTraversalRecursion(source, visited);
//     }
// }


// public class BFS {
//     public static void main(String[] args) {
//         Graph graph = new Graph(4, true);

//         graph.addEdge(0, 1);
//         graph.addEdge(1, 4);
//         graph.addEdge(3, 2);
//         graph.addEdge(3, 1);

//         graph.printList();
//     }
    
// }




import java.util.*;


class Graph{
    ArrayList<ArrayList<Integer>> adjList;
    boolean undirected;
    int v;

    Graph(int v, boolean undirected) {
        this.v = v;
        this.undirected = undirected;
        adjList = new ArrayList<ArrayList<Integer>>(v);

        for (int i = 0; i < v; i++) {
            adjList.add(new ArrayList<Integer>());
        }
    }

    void addEdge(int a, int b){
        adjList.get(a).add(b);
        if(this.undirected){
            adjList.get(b).add(a);
        }
    }

    void printList(){
        for (int i = 0; i < adjList.size(); i++) {
            System.out.print(i+" ---> ");

            for (int j = 0; j < adjList.get(i).size(); j++) {
                System.out.print(adjList.get(i).get(j)+", ");    
            }
            System.out.println("");
        }
    }

    boolean has_cycle(){
        boolean[] visited = new boolean[v];
        return hasCycleUsingDFS(0, -1, visited);
    }

    boolean hasCycleUsingDFS(int node, int parent, boolean[] visited){ 
        visited[node] = true;

        //traverse through all of node's neigbours
        System.out.println("Now visiting: "+node);

        for(int i = 0; i < adjList.get(node).size(); i++){ 
            int neigbour = adjList.get(node).get(i);
            System.out.println("Now at "+neigbour);
            if(!visited[neigbour]){ 
                //node is the new parent
                boolean neighbourHasFoundACycle = hasCycleUsingDFS(neigbour,node, visited);
                System.out.println(neigbour+" has returned "+neighbourHasFoundACycle); 
                if(neighbourHasFoundACycle) return true;
            }
            //Visited but its not parent, a parent and child don't make a cycle.
            else if(neigbour!=parent){ return true; } 
        }
        //Visited, but a not parent
        return false;
    }

    void DFSTraversalRecursion(int node, boolean visited[]){
        visited[node] = true;
        System.out.print(node+" -> ");

        
        for(int i=0; i< adjList.get(node).size(); i++){  // for (int nbr : adjList.get(node)) DOES THIS WORK?  
            int neighbour = adjList.get(node).get(i);
            if(!visited[neighbour])
                DFSTraversalRecursion(neighbour, visited);
        }
    }
    
    void DFSTraversal(int source){
        boolean[] visited = new boolean[v];
        DFSTraversalRecursion(source, visited);
    }
}



public class DFS {
    public static void main(String[] args) {
        Graph graph = new Graph(10, true);

        // graph.addEdge(0, 1);
        graph.addEdge(0, 1);
        graph.addEdge(0, 7);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 4);
        graph.addEdge(2, 5);

        graph.addEdge(7, 8);
        graph.addEdge(5, 6);  
        graph.addEdge(7, 9);


        graph.printList();
        graph.DFSTraversal(0);

        // if(graph.has_cycle())
        //     System.out.println("Has Cycle!");
        // else
        //     System.out.println("Doesn't have a cycle.");

        // graph.shortestPathBetween(0,4);
    }
    
}