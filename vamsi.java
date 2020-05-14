import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main (String[] args) {
        //code
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        while(t-- != 0) {

            String s = sc.nextLine();
            if(s.length() == 1) {
                System.out.println(s);
                continue;
            }


            char temp = '!';
            int i = 1;
            char[] ans = new char[s.length()];
            int top = -1;
            int l = 0;
            while(i < s.length()) {
                if(s.charAt(l) == temp) {
                    l++;i++;continue;
                }
                while(i < s.length() && s.charAt(i) == s.charAt(l))
                    i++;
                if(i == s.length()) break;
                if(i - l == 1) {
                    if(top != -1 && ans[top] == s.charAt(l)) {
                        temp = ans[top];
                        top--;
                    }
                    else  {
                        ans[++top] = s.charAt(l);
                        temp = '!';
                    }
                }
                l = i;
                i++;
            }



            int len = s.length();
            if(s.charAt(len -1) != s.charAt(len -2)) {
                char c = s.charAt(len-1);
                if(top == -1) {
                    ans[++top] = s.charAt(len-1);
                    temp = '!';
                }
                else if(temp == c);
                else if(c == ans[top]) top--;
                else {
                    // temp = ans[top];
                    // top--;
                    ans[++top] = c;
                }
            }
            
            for(int k = 0; k <= top; k++) {
                System.out.print(ans[k]);
            }
            System.out.println();
        }
    }
}