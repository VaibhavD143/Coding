import java.util.*;
class Solution {

    public static String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder();
        int carry = 0;
        int i1 = a.length()-1,i2=b.length()-1;
        int sm;
        while(i1>=0 && i2>=0){
            sm = carry+Character.getNumericValue(a.charAt(i1))+Character.getNumericValue(b.charAt(i2));
            res.append(getBit(sm));
            carry = sm>1?1:0;
            i1--;i2--;

        }
        while(i1>=0){
            sm = carry+Character.getNumericValue(a.charAt(i1));
            res.append(getBit(sm));
            carry = sm > 1 ? 1 : 0;
            i1--;
        }
        while (i2 >= 0) {
            sm = carry + Character.getNumericValue(b.charAt(i2));
            res.append(getBit(sm));
            carry = sm > 1 ? 1 : 0;
            i2--;
        }
        if (carry == 1) {
            res.append(1);
        }
        StringBuffer bf = new StringBuffer(res);
        return bf.reverse().toString();

    }

    public static int getBit(int n) {
        if(n==2){
            return 0;
        }
        else if(n==3){
            return 1;
        }
        return n;
    }
    public static void main(String[] args) {
        // System.out.println(Solution.addBinary("11", "1"));        
        System.out.println(Solution.addBinary("1010", "1011"));        
    }
}