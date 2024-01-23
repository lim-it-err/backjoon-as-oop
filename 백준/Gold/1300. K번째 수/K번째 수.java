import java.util.Scanner;

import static java.lang.Math.min;

public class Main {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        long M = sc.nextLong();
        binarySearch(0, N*N, N, M);
    }
    public static void binarySearch(long src, long dst, long N, long M){
        long cur = (src+dst)/2;
        long cur_value = findKIndex(cur, N);
//        System.out.println(src+" "+dst+" "+cur+" "+cur_value);
        if ((isExist(cur, N) &&src==dst) || (isExist(cur, N)&&cur_value == M)) {
            System.out.println(cur);
            System.exit(0);
        }
        else if (cur_value == M){
            binarySearch(src, cur-1, N, M);
        }
        else if (cur_value>M) {
            binarySearch(src, cur, N, M);
        }
        else {
            binarySearch((src+dst+1)/2, dst, N, M);
        }
    }
    public static long findKIndex(long num, long N)
    {
        long retValue = 0;
        for (long i = 1 ; i <= N ; i++ ) retValue+=min(num/i, N);
//        System.out.println("Called,"+ num+" "+ retValue);
        return retValue;
    }
    public static boolean isExist(long num, long N)
    {
        if (num <=N) return true;
        for(long i = 2; i <= N ; i++) if(num%i==0 && num/i<=N) return true;
        return false;
    }
}
