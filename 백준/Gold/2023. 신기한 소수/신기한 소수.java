import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    static Map<Integer, Boolean> primeMap = new HashMap<Integer, Boolean>();
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int result = 0;
         DFS(2, N);
        DFS(3, N);
        DFS(5, N);
        DFS(7, N);
    }
    public static void DFS(int prevNum, int digitNum)
    {
        if (!isPrime(prevNum)) return;
        if (prevNum - Math.pow(10, digitNum)/10>0) {
            System.out.println(prevNum);
            return;
        }
        for (int i = 1 ; i < 10 ; i++) {
            if (i % 2 == 0) continue;
            DFS(prevNum*10+i, digitNum);
        }
    }
    private static boolean isPrime(int num){
        if (primeMap.get(num)!=null && primeMap.get(num))  return true;
        for (int i = 2 ; i *i <= num ; i++)
        {
            if (num%i ==0) return false;
        }
        return true;
    }
}
