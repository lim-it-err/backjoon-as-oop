import java.util.*;

public class Main {
    public static class MyPair<A extends Comparable<A>, B extends Comparable<B>> implements Comparable<MyPair<A, B>> {
    private A first;
    private B second;

    public MyPair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    public A getFirst() {
        return first;
    }

    public B getSecond() {
        return second;
    }

    public void setFirst(A first) {
        this.first = first;
    }

    public void setSecond(B second) {
        this.second = second;
    }
    @Override
    public int compareTo(MyPair<A, B> other) {
        int firstCompare = this.first.compareTo(other.first);
        if (firstCompare != 0) {
            return firstCompare;
        } else {
            return this.second.compareTo(other.second);
        }
    }

    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<MyPair< Integer, Integer>> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int first = sc.nextInt();
            int second = sc.nextInt();
            arr.add(new MyPair<>(first, second));
        }
        Collections.sort(arr);
        int count = 0;
        int cur = 0;
        while (cur <N && cur>=0){
            cur = getIdxOfMinimum(arr, cur);
            count +=1;
//            System.out.println(cur);
        }
        System.out.println(count);
    }
    public static int getIdxOfMinimum(ArrayList<MyPair<Integer, Integer>> arr, int start_idx) {
        double minValue = Math.pow(2, 31);
        for (int i = start_idx; i < arr.size(); i++) {
            if (arr.get(i).getFirst() >= minValue) return i;
            if (arr.get(i).getSecond() < minValue) {
                minValue = arr.get(i).getSecond();
            }
        }
        return -1;
    }
}

