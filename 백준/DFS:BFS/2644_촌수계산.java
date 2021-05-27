import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int p1,p2,n;
    static boolean[] visited;
    static int[] count;
    static ArrayList<ArrayList<Integer>> graph;
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        String[] inputs = bf.readLine().split(" ");
        int start = Integer.parseInt(inputs[0]);
        int end = Integer.parseInt(inputs[1]);

        int m = Integer.parseInt(bf.readLine());

        visited = new boolean[n+1];
        count = new int[n+1];
        graph = new ArrayList<ArrayList<Integer>>();

        for(int i=0; i<n+1; i++) {
            graph.add(new ArrayList<Integer>());
        }

        for(int i=0;i<m;i++){
            inputs = bf.readLine().split(" ");
            int p1 = Integer.parseInt(inputs[0]);
            int p2 = Integer.parseInt(inputs[1]);

            graph.get(p1).add(p2);
            graph.get(p2).add(p1);
        }
        System.out.println(bfs(start,end));
    }

    private static int bfs(int start,int end){
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(start);
        visited[start] = true;
        while(!queue.isEmpty()){
            int now = queue.poll();
            if (now == end){
                return count[now];
            }
            for(int i=0;i<graph.get(now).size();i++){
                int value = graph.get(now).get(i);
                if(visited[value]!=true){
                    queue.add(value);
                    count[value] = count[now] + 1;
                    visited[value] = true;
                }
            }
        }
        return -1;
    }
}