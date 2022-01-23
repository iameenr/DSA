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
            System.out.print(adjList.get(i).get(0)+" ---> ");

            for (int j = 1; j < adjList.get(i).size(); j++) {
                System.out.print(adjList.get(i).get(j)+", ");    
            }
            System.out.println("");
        }
    }

    int[] shortestPathBFS(int source){
        //Visited arrays a
        boolean[] visited = new boolean[v];
        

        Queue<Integer>  q = new LinkedList<Integer>();
        q.add(source);
        visited[source] = true;

        //Creating Array for keeping shortest path 
        int[] shortestPath = new int[v];
        //Array to backtrack parent
        int[] parent = new int[v];

        //Because shortest path from 0 to 0 is 0 which will be initialized when 1 gets added
        shortestPath[0] = -1;

        while(!q.isEmpty()){
            int vertex = q.remove();
            //Shortest path for this vertex is the shortest path of its parent plus 1
            shortestPath[vertex] = shortestPath[parent[vertex]] +1; 
            System.out.print(vertex+" -> ");
            for (int i = 0; i < adjList.get(vertex).size(); i++) {
                int nodeNow = adjList.get(vertex).get(i);
                if(!visited[nodeNow]){
                    q.add(nodeNow);
                    //Adding the parent of the node in consideration
                    parent[nodeNow] = vertex;
                    visited[nodeNow] = true;
                }
            }
        }
        
        for (int i=0; i<v; i++) {
            System.out.println("Shortest path from Source to "+i+" is "+shortestPath[i]);
        }
        return parent;
    }

    void shortestPathBetween(int from, int destination){
        int[] parent = new int[v];
        parent = shortestPathBFS(from);

        int i = destination;
        System.out.print("Shortest path from source to "+destination+" is: "+destination+" -> ");
        while(i!=from){
            System.out.print(parent[i]+" -> ");
            i = parent[i]; 
        }
    }
}


public class ShortestPathBetweenTwoVertices {
    public static void main(String[] args) {
        Graph graph = new Graph(6, true);

        graph.addEdge(0, 1);
        graph.addEdge(0, 3);
        graph.addEdge(1, 2);
        graph.addEdge(1, 5);
        graph.addEdge(2, 3);  
        graph.addEdge(4, 5);


        graph.printList();
        graph.shortestPathBetween(0,4);
    }
    
}