

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] sum = new int[N];
        sum[0] = sc.nextInt();
        for (int i = 1; i < N; i++) {
            sum[i] = sum[i - 1] + sc.nextInt();
        }
        for (int i = 0; i < M; i++) {
            int src = sc.nextInt();
            int dst = sc.nextInt();
            int result = calculatePartialSum(N, sum, src, dst);
            System.out.println(result);
        }
    }

    // 부분합을 계산하는 메서드
    public static int calculatePartialSum(int N, int[] sum, int src, int dst) {
        if (src == 1) {
            return sum[dst - 1];
        } else {
            return sum[dst - 1] - sum[src - 2];
        }
    }
}
