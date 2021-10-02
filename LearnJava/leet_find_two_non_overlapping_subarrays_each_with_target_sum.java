class Solution {
    public int minSumOfLengths1(int[] arr, int target) {
        int res = Integer.MAX_VALUE;
        int[] pref = new int[arr.length+1];
        pref[0] = Integer.MAX_VALUE;
        Map<Integer,Integer> ha  = new HashMap<>();
        ha.put(0,0);
        int sm=0;
        for(int i=0;i<arr.length;i++){
            sm+=arr[i];
            if(ha.containsKey(sm-target)){
                int ind = ha.get(sm-target);
                res = pref[ind]!=Integer.MAX_VALUE?Math.min(res,i-ind+1+pref[ind]):res;
                pref[i+1] = Math.min(i-ind+1,pref[i]);
                // System.out.println(res);
            }
            else{
                pref[i+1] = pref[i];
            }
            ha.put(sm,i+1);
        }
        // System.out.println(ha);
        return res!=Integer.MAX_VALUE?res:-1;
    }
   public int minSumOfLengths(int[] arr, int target) {
        int res = Integer.MAX_VALUE;
        int[] pref = new int[arr.length+1];
        Arrays.fill(pref,Integer.MAX_VALUE);
        int sm=0,left=0,right,tmp;
        for(right=0;right<arr.length;right++){
            sm+=arr[right];
            while(sm>target)sm-=arr[left++];
            
            if(sm == target){
                // System.out.print(right);
                // System.out.print(left);
                // System.out.println(Arrays.toString(pref));
                tmp = right-left+1;
                if(pref[left] != Integer.MAX_VALUE){
                    res = Math.min(res,tmp+pref[left]);    
                }
                pref[right+1] = Math.min(pref[right],tmp);
            }
            else{
                pref[right+1] = pref[right];
            }
        }
        // System.out.println(ha);
        return res!=Integer.MAX_VALUE?res:-1;
    }
}