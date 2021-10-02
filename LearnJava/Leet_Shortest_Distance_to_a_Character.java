class Solution {
    public int[] shortestToChar(String s, char c) {
        int[] result = new int[s.length()];
        Arrays.fill(result, Integer.MAX_VALUE);
        
        int curr = Integer.MAX_VALUE;
        
        // System.out.println(Arrays.toString(result));
        for (int i = 0; i < result.length; i++) {
            if (s.charAt(i) == c) {
                curr = 0;
            }
            result[i] = Math.min(result[i], curr);
            curr = curr == Integer.MAX_VALUE ? curr : curr+1;
        }
        
        // System.out.println(Arrays.toString(result));
        
        curr = Integer.MAX_VALUE;
        
        for (int i = result.length - 1; i >= 0; i--) {
            if (s.charAt(i) == c) {
                curr = 0;
            }
            
            result[i] = Math.min(result[i], curr);
            curr = curr == Integer.MAX_VALUE ? curr : curr+1;
        }
        
        return result;
        
    }
}