class Leet_Longest_Harmonious_Subsequence {
    public int findLHS(int[] nums) {
        HashMap<Integer, Integer> cnt = new HashMap<Integer, Integer>();
        
        for (int i = 0; i < nums.length; i++) {
            cnt.put(nums[i], cnt.getOrDefault(nums[i], 0) + 1);
        }
        
        int ans = 0;
        
        for (Integer key : cnt.keySet()) {
            ans = Math.max(ans, cnt.get(key) + cnt.getOrDefault(key - 1, Integer.MIN_VALUE));
        }
        
        return ans;
    }
}