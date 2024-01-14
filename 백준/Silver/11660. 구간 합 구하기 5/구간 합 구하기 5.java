import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        int[][] arr= new int[N+1][N+1];
        for (int i = 1 ; i <= N ; i++){
            for (int j = 1 ; j <= N ;j++){
                arr[i][j] = sc.nextInt();
            }
        }

        int[][] sum_board = new int[N+1][N+1];
        for(int i = 1 ; i <= N ; i++)
            for(int j = 1 ; j <= N ; j++){
                sum_board[i][j] = -sum_board[i-1][j-1] + sum_board[i-1][j]+sum_board[i][j-1]+arr[i][j];
            }

        for (int i = 0 ; i < M ; i++){
            int X1 = sc.nextInt();
            int Y1 = sc.nextInt();
            int X2 = sc.nextInt();
            int Y2 = sc.nextInt();
            System.out.println(sum_board[X2][Y2]-sum_board[X1-1][Y2]-sum_board[X2][Y1-1]+sum_board[X1-1][Y1-1]);

        }
    }

}
