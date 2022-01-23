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

}


public class GraphUsingAdjList {
    public static void main(String[] args) {
        Graph graph = new Graph(4, true);

        graph.addEdge(0, 1);
        graph.addEdge(1, 4);
        graph.addEdge(3, 2);
        graph.addEdge(3, 1);

        graph.printList();
    }
    
}