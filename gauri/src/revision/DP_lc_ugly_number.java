package revision;

//https://leetcode.com/problems/ugly-number/submissions/
public class DP_lc_ugly_number {

	 public boolean isUgly(int num) {
	        if(num<=0)
	            return false;
	        else if(num<=3 || num==5)
	            return true;
	        else if(num%2==0)
	            return isUgly(num/2);
	        
	        else if(num%3==0)
	            return isUgly(num/3);
	        
	        else if(num%5==0)
	            return isUgly(num/5);
	        
	        return false;
	    }
}
