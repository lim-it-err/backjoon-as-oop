import java.util.Scanner;

public class Main {
    private static int[] arr = new int[100];

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt(); // Number of coins
        int K = scanner.nextInt(); // Total value

        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

        int sum = 0;
        for (int i = N - 1; i >= 0; i--) {
            sum += K / arr[i]; // Counting coins
            K = K % arr[i]; // Remaining value
        }

        System.out.println(sum); // Output the result
    }
}
