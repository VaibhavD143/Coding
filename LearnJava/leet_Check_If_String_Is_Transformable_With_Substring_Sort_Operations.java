/*
Intution: we collect indices of each integer in our original string `s` and then we iterate through our target string `t`,
check if any smaller than target integer is present between current index and target index.
*/
import java.util.*;

class Solution {
    public static boolean isTransformable(String s, String t) {
        LinkedList<Integer> ind[] = new LinkedList[10];
        for(int i=0;i<ind.length;i++)
            ind[i] = new LinkedList<>();
        for(int i=0;i<s.length();i++){
            int n = s.charAt(i)-'0';
            System.out.println(n);
            ind[n].offer(i);
        }
        for(int i=0;i<ind.length;i++)
        {
            System.out.println(ind[i].toString());
        }
        int n;
        for(int i=0;i<t.length();i++){
            n = t.charAt(i)-'0';
            if(ind[n].size()==0){
                return false;
            }
            for(int j=n-1;j>=0;j--){
                if(ind[j].size()>0 && ind[j].getFirst()<ind[n].getFirst()){
                    return false;
                }
            }
            ind[n].poll();
        }
        return true;
    }

    public static void main(String[] args) {
        // System.out.println(Solution.isTransformable(new String("84532"),new String("34852")));
        // System.out.println(Solution.isTransformable(new String("34521"),new String("23415")));
        // System.out.println(Solution.isTransformable(new String("12345"),new String("12435")));
        System.out.println(Solution.isTransformable(new String("123"),new String("1123")));
    }
}