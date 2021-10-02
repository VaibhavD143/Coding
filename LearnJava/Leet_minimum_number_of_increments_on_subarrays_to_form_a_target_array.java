public class Leet_minimum_number_of_increments_on_subarrays_to_form_a_target_array {
    public static int minNumberOperations(int[] target) {
        int cnt=target[0];
        for(int i=1;i<target.length;i++){
            cnt+=Math.max(target[i]-target[i-1],0);
        }
        return cnt;       
    }

    public static void main(String[] args) {
        System.out.println(minNumberOperations(new int[]{3,1,5,4,2}));
    }
}
