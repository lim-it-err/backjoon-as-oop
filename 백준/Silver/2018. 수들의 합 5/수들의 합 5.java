import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int cur = 0;
        int left = 0;
        int right = 0;
        int result = 0;
        while (right <= N)
        {
            if (N == cur)   result +=1;
            if (N >= cur) {
                right += 1;
                cur += right;
            }
            else if (N < cur) {
                left += 1;
                cur -= left;
            }
//            System.out.println(left+" "+right+" "+cur);
        }
        System.out.println(result);
    }
}
