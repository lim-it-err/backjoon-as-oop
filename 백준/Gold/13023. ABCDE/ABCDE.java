import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static HashMap<Integer, List<Integer>> friendMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int src = Integer.parseInt(st.nextToken());
            int dst = Integer.parseInt(st.nextToken());
            friendMap.putIfAbsent(src, new ArrayList<>());
            friendMap.get(src).add(dst);
            friendMap.putIfAbsent(dst, new ArrayList<>());
            friendMap.get(dst).add(src);
        }
        for (int i = 1; i <= N; i++) {
            if (friendMap.get(i) == null) continue;
            List<Integer> lst = friendMap.get(i);
            for (int j : lst) {
                List<Integer> friend_lst = new ArrayList<>();
                friend_lst.add(j);
                DFS(friend_lst);
            }
        }
        System.out.println(0);
    }

    public static boolean DFS(List<Integer> history) {
        if (history.size() == 5) {
            System.out.println("1");
            System.exit(0);
        }
        int current = history.get(history.size() - 1);
        List<Integer> lst = friendMap.get(current);
        for (int i : lst) {
            if (history.contains(i)) continue;
            List<Integer> new_history = new ArrayList<>(history);
            new_history.add(i);
            DFS(new_history);
        }

        return false;
    }

}
