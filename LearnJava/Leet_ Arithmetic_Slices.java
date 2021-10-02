class Leet_Arithmetic_Slices {
    public int numberOfArithmeticSlices(int[] nums) {
        int res = 0;
        
        int i = 0;
        Integer a;
        while (i < nums.length-2) {
            int len = 0;
            int diff = nums[i+1] - nums[i];
            int end = i;
            while (end < nums.length - 1 && nums[end + 1] - nums[end] == diff ) {
                end++;
            }
            if (end - i + 1 >= 3){
                len = end - i + 1;
                res += (((len * (len + 1)) / 2) - len - len + 1);
            }
            i = end;
            
        }
        
        return res;
    }

    public static void main(String[] args) {
      Leet_Arithmetic_Slices obj = new Leet_Arithmetic_Slices();
      System.out.println(obj.numberOfArithmeticSlices(new int[]{1, 2, 3}));
    }
}
