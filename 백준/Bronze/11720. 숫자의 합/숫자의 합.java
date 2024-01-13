import java.util.Scanner;

public class Main{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int sum = solution(N, sc.next());

        System.out.print(sum);
    }
    public static int solution(int N, String sNum){
        char[] cNum = sNum.toCharArray();
        int sum = 0;
        for (int i = 0; i< cNum.length;i++)
        {
            sum+= cNum[i]-'0';
        }
        return sum;
    }
}
