import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int target = sc.nextInt();
        int[] content = new int[N];
        for (int i = 0 ; i < N ; i++)   content[i] = sc.nextInt();
        Arrays.sort(content);

        int left_ptr = 0;
        int right_ptr = N-1;
        int answer = 0;
        while (left_ptr<right_ptr){
            if (content[right_ptr]+content[left_ptr] == target) answer +=1;
            if (content[right_ptr]+content[left_ptr]>target)    {right_ptr-=1; }
            else                { left_ptr +=1;}
        }
        System.out.println(answer);
    }
}
/* Testcase
6 9
1 2 2 4 5 7
Expected : 3
 */
