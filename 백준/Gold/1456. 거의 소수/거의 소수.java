import java.util.*;

public class Main{
    static ArrayList<Long> arr = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long M = sc.nextLong();
        arr.add(2L);
        for (long i = 3; i*i <= M; i+=2)
        {
            if (isPrime(i)) arr.add(i);
        }
        long answer = 0;
        for (long number:arr){
            for (long i = 2 ; Math.pow(number, i)<=M; i++){
                if (Math.pow(number, i)>=N) answer+=1;
            }
        }
        System.out.println(answer);
    }
    public static boolean isPrime(long num){
        for (long i : arr) {
            if (i * i > num) break;
            if (num % i == 0)
                return false;
        }
        return true;
    }
}