import java.io.*; 
import java.util.*;

public class Main {
    static int n,m,c;
    static boolean[] visited;
    static int[] count;
    static ArrayList<ArrayList<Integer>> graph;
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int m = Integer.parseInt(bf.readLine());
        String[] inputs = bf.readLine().split(" ");
        graph = new ArrayList<ArrayList<Integer>>();

        visited = new boolean[n+1];
        count = new int[n+1];
        c = 0;

        for(int i=0; i<n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for(int i=0; i<m-1; i++){
            inputs = bf.readLine().split(" ");
            int p1 = Integer.parseInt(inputs[0]);
            int p2 = Integer.parseInt(inputs[1]);

            graph.get(p1).add(p2);
            graph.get(p2).add(p1);
        }
        bfs(1);

        for(int i=2; i<count.length;i++){
            if(count[i]<=2 && count[i] != 0){
                c += 1;
            }
        }
        System.out.println(c);
    }

    public static void bfs(int start){
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start);
        visited[start] = true;
        while(!queue.isEmpty()){
            int now = queue.poll();
            for(int i=0;i<graph.get(now).size();i++){
                int value = graph.get(now).get(i);
                if(visited[value]!=true){
                    queue.add(value);
                    count[value] = count[now] + 1;
                    visited[value] = true;
                }
            }
        }
    }
}