import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0 ; i < N; i++)
        {
            arr[i] = sc.nextInt();
        }
        System.out.println(solution(N, arr));

    }
    public static float solution(int N, int[] arr)
    {
        float sum = 0;
        int maximum = -1;
        for (int single_arr:arr){
            sum+=single_arr;
            if (maximum < single_arr){
                maximum = single_arr;
            }
        }
        return sum / N * 100/ maximum;
    }
}