import java.util.Scanner;

public class Main {
    static final int MAX_N = 500001;
    static int n;
    static int[] numbers;
    static long[] arr2;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        numbers = new int[n];
        arr2 = new long[MAX_N];

        for (int i = 0; i < n; i++) {
            int temp = scanner.nextInt();
            numbers[i] = temp;
        }

        long answer = navigate(0, n - 1);
        System.out.println(answer);
    }

    static long navigate(int start, int end) {
        if (start == end)
            return 0;

        int mid = (start + end) / 2;
        long answer = navigate(start, mid) + navigate(mid + 1, end);

        int i = start, j = mid + 1;
        int idx = 0;

        while (i <= mid || j <= end) {
            if (i <= mid && ((j > end) || numbers[i] <= numbers[j])) {
                arr2[idx++] = numbers[i++];
            } else {
                answer += (long) (mid - i + 1);
                arr2[idx++] = numbers[j++];
            }
        }

        for (int k = start; k <= end; k++) {
            numbers[k] = (int) arr2[k - start];
        }

        return answer;
    }
}
