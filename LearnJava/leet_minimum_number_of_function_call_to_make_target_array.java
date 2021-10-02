class Solution {
    public int minOperations(int[] nums) {
        int res=0,max_even =0,odd,even;
        for(int num:nums){
            odd=0;even = 0;
            
            while(num>0){
                if((num&(1)) == 1)odd++;
                if(num>1)even++;
                num=num>>1;
                // System.out.println(num);
            }
            res+=odd;
            max_even = Math.max(max_even,even);
        }
        return res+max_even;
    }
}