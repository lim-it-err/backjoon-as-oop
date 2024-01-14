import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] arr = new long[N+1];
        long counter = 0;
        for (int i = 1; i <= N; i++) {
            arr[i] = arr[i - 1] + sc.nextInt();
        }
        long[] count_frequency = new long[M];
        for (int i = 1 ; i <=N ; i++) {
            if ((arr[i] % M) == 0) {
                counter += 1;
            }
            count_frequency[(int)(arr[i]%(long)M)] +=1 ;
        }
        for (int i = 0 ; i < M ; i++){
            if( count_frequency[i]>=2)
                counter += count_frequency[i]*(count_frequency[i]-1)/2;
        }
        System.out.println(counter);
    }
}
//3 2 1 2 2
//3 5 6 8 10 == 0 2 0 2 1 -> 1+1+2C2+2C2
