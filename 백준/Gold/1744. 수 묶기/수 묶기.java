import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> plusArr = new ArrayList<>();
        ArrayList<Integer> minusArr = new ArrayList<>();
        for (int i = 0 ; i < N ;i++){
            int item = sc.nextInt();
            if (item>0)    plusArr.add(item);
            else            minusArr.add(item);
        }
        Collections.sort(plusArr, Collections.reverseOrder());
        Collections.sort(minusArr);
        int answer = 0;
        for (int i = 0 ; i+1 < plusArr.size(); i+=2)
        {
            int first = plusArr.get(i);
            int second = plusArr.get(i+1);
            if (first <=1 || second <=1)    answer+=(first+second);
            else answer+=(first*second);
//            System.out.println(answer);
        }
        if (plusArr.size()%2==1)    answer+=plusArr.get(plusArr.size()-1);
        for (int i = 0 ; i+1 < minusArr.size(); i+=2)
        {
            int first = minusArr.get(i);
            int second = minusArr.get(i+1);
            answer+=(first*second);
        }
        if (minusArr.size()%2==1)    answer+=minusArr.get(minusArr.size()-1);

        System.out.println(answer);
    }

}
