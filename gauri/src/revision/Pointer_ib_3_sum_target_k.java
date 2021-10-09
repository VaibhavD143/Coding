package revision;
import java.util.*;
//https://www.interviewbit.com/problems/3-sum/
/*concept:
 * for condition: a+b+c=0;
 * we put sum as -c and then use two pointer method to find if condition is true anywhere.
 * For target ie. a+b+c=target, put sum as target-c and then use two pointer to calculate if for any 
 * a+b, we get the sum as target-c;
 */
public class Pointer_ib_3_sum_target_k {
    public int threeSumClosest(int[] a, int k) {
        long ans=Integer.MAX_VALUE;
        Arrays.sort(a);
        outer:for(int i=0;i<=a.length-2;++i){
            int l=i+1,r=a.length-1;
            long sum=k-a[i];
            while(l<r){
                long tsum=a[l]+a[r];
                if(Math.abs(ans-k)>Math.abs(tsum-sum))
                    ans=a[l]+a[r]+a[i];
                if(tsum==sum)
                    break outer;
                else if(tsum<sum)
                    ++l;
                else
                    --r;
            }
        }
        return (int)ans;
    }
}
