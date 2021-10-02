public class Leet_jump_game_2 {
    public static int jump(int[] nums) {
        int cnt=0;
        int cur_reach = 0;
        int i=0;
        while(cur_reach<nums.length-1){
            int nxt_reach = 0;
            // int ind = 0;
            while(i<nums.length && i<=cur_reach){
                // if (nxt_reach<=i+nums[i]){
                //     nxt_reach = i+nums[i];
                //     ind = i;
                // }
                nxt_reach = Math.max(nxt_reach,i+nums[i]);
                i++;
            }
            cur_reach = nxt_reach;
            // i = ind;
            cnt++;
        }
        return cnt;
            
    }

    public static void main(String[] args) {
        System.out.println(jump(new int[]{2,3,0,1}));
    }
}