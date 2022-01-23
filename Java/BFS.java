import java.util.concurrent.ForkJoinPool;

import javax.sound.sampled.SourceDataLine;

class Graph{
        ArrayList<ArrayList<Integers>> adjList;
        boolean undirected;

        Graph(int v, boolean undirected) {
            this.undirected = undirected;
            adjList = new ArrayList<ArrayList<Integers>>(5);

            for (int i = 0; i < adjList.size(); i++) {
                adjList.get(i) = new ArrayList<Integers>();
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
                System.out.println(adjList.get(i)+" ---> ");

                for (int j = 0; j < adjList.get(i).size(); j++) {
                    System.out.print(adjList.get(i).get(j)+", ");    
                }
                System.out.println("");
            }
        }

        void BFSTraversal(int source){
            //Visited arrays a
            boolean visited[v];
            Queue<Integers>  q = new LinkedList<Integers>();
            q.add(source);
            visited[source] = true;

            while(!q.isEmpty()){
                int vertex = q.remove();

                System.out.print("\n"+vertex+" -> ");

                for (int i = 0; i < q.get(vertex).size(); i++) {
                    int nodeNow = adjList.get(vertex).get(i);
                    if(!visited[nodeNow]){
                        q.add(nodeNow);
                        visited[nodeNow] = true;
                }
            }
        }
    }

    void DFSTraversalRecursion(int node, boolean visited[]){
        visited[node] = true;
        System.out.println(node+" -> ");

        while(!visited[node]){
            for(int i=0; i< adjList.get(node).size(); i++){  // for (int nbr : adjList.get(node)) DOES THIS WORK?  
                int neighbour = adjList.get(node).get(i);
                DFSTraversalRecursion(neighbour, visited)
            }
        }
    }

    void DFSTraversal(int source){
        boolean visited[v];
        DFSTraversalRecursion(source, visited);
    }
}


public class BFS {
    public static void main(String[] args) {
        Graph graph = new Graph(4, true);

        graph.addEdge(0, 1);
        graph.addEdge(1, 4);
        graph.addEdge(3, 2);
        graph.addEdge(3, 1);

        graph.printList();
    }
    
}