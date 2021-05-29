import java.io.*; 
import java.util.*;

class Pairs {
    int x;
    int y;

    Pairs(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class App {
    static int w,h,count;
    static boolean[][] visited;
    static int[][] map;
    static int[] dx = {-1,1,0,0,1,-1,1,-1};
    static int[] dy = {0,0,-1,1,1,-1,-1,1};
    public static void main(String[] args) throws Exception{
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> result = new ArrayList<>();

        while(true){    
            w = sc.nextInt();
            h = sc.nextInt();
            if(w==0 && h==0){
                break;
            }
            count = 0;
            map = new int[h][w];
            visited = new boolean[h][w];

            for(int i=0;i<h;i++){
                for(int j=0;j<w;j++){
                    map[i][j] = sc.nextInt();
                }
            }   

            for(int i=0;i<h;i++){
                for(int j=0;j<w;j++){
                    if(visited[i][j] ==false && map[i][j]==1){
                        count += bfs(i,j,map,visited);
                    }
                }
            }
            result.add(count);
        }
        for(int i=0;i<result.size();i++){
            System.out.println(result.get(i));
        } 
    }

    public static int bfs(int start_x, int start_y, int[][] m, boolean[][] visit){
        Queue<Pairs> queue = new LinkedList<Pairs>();
        queue.add(new Pairs(start_x, start_y));
        visited[start_x][start_y] = true;
        while(!queue.isEmpty()){
            Pairs p = queue.remove();
            for(int i=0;i<8;i++){
                int nx = p.x+dx[i];
                int ny = p.y+dy[i];
                if(0<=nx && nx<h && 0<=ny && ny<w && visit[nx][ny] == false && m[nx][ny]==1){
                    visit[nx][ny] = true;
                    queue.add(new Pairs(nx, ny));
                }
            }
        }
        return 1;
    }
}