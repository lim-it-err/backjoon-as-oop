import java.sql.Array;
import java.util.*;
import java.util.HashMap;
public class Main {

    static int[] arr;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int T = sc.nextInt();
        arr = new int[N];
        for (int i = 0 ; i < N; i++)arr[i] = i;
        int[] truthUser = new int[T];
        boolean[] visited = new boolean[N];
        for (int i = 0; i < T; i++) truthUser[i] = sc.nextInt()-1;
        // 1. Graph를 생성한 후 -> BFS 돌린 후 visited 조사하면 끝!
        // Graph 생성 : 1. Adjacency List(Hashmap) / 2. Adjacency Matrix
        ArrayList<Integer>[] brr = new ArrayList[M];
        for(int i = 0 ; i < M ; i++) brr[i] = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            int group_num = sc.nextInt();
            for (int j = 0; j < group_num; j++) brr[i].add(sc.nextInt()-1);
            makeParentinCompleteGraph(brr[i]);
        }
        for (int user : truthUser) {
            int idx = arr[user];
            for (int i = 0; i < arr.length; i++) {
                if (findParent(arr[i]) == findParent(idx)) visited[i] = true;
            }
        }
        int answer = 0;
        boolean flag = false;
        for (int i = 0 ; i < M ; i++){
            for (int user : brr[i]) {
                if (visited[user]) {
                    flag = true;
                    break;
            }
            }
            if (!flag)
                answer++;
            flag = false;
        }
        System.out.println(answer);
//        for (int ar :arr) System.out.print(ar+" ");
    }

    static void makeParentinCompleteGraph(ArrayList<Integer> users) {
        for (int i = 0 ; i < users.size();i++)
            for (Integer user : users) union(users.get(i), user);
    }

    static int findParent(int i) {
        if (arr[i] == i) return i;
        return arr[i] = findParent(arr[i]);
    }
    static void union(int user1, int user2) {
        /*
        description: merge user2's group into user1`s group
         */
        arr[findParent(user2)] = findParent(user1);
    }


    }


//    10 9
//            1 1
//            2 5 6
//            2 4 5
//            2 3 4
//            2 2 3
//            2 1 2
//            2 9 10
//            2 8 9
//            2 7 8
//            2 6 7