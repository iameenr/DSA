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
}


public class CycleDetectionInUndirectedGraphUsingDFS {
    public static void main(String[] args) {
        Graph graph = new Graph(4, true);

        // graph.addEdge(0, 1);
        graph.addEdge(0, 3);
        graph.addEdge(1, 2);
        // graph.addEdge(0, 1);
        // graph.addEdge(1, 5);
        graph.addEdge(2, 3);  
        // graph.addEdge(1, 3);


        graph.printList();
        if(graph.has_cycle())
            System.out.println("Has Cycle!");
        else
            System.out.println("Doesn't have a cycle.");

        // graph.shortestPathBetween(0,4);
    }
    
}