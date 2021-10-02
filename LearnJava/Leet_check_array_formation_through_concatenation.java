import java.util.Arrays;
import java.util.HashMap;

/**
 * leet_check_array_formation_through_concatenation
 */
public class Leet_check_array_formation_through_concatenation {
    public static void main(String[] args) {
        canFormArray(new int[]{18}, new int[][]{new int[]{18}});
    }

    public static boolean canFormArray(int[] arr, int[][] pieces) {
        System.out.println(Arrays.toString(arr));
        System.out.println(Arrays.deepToString(pieces));
        HashMap<Integer,Integer> ha = new HashMap<>();
        
        for(int i=0;i<arr.length;i++){
            ha.put(arr[i],i);
        }
        int cnt = arr.length;
        for(int i=0;i<pieces.length;i++){
            if(!ha.containsKey(pieces[i][0])){
                return false;
            }
            int ind = ha.get(pieces[i][0]);
            for(int j=0;j<pieces[i].length;j++){
                if(ind+j>=arr.length || arr[ind+j]!=pieces[i][j]){
                    return false;
                }
            }
            cnt-=pieces[i].length;
        }
        if(cnt ==0){
            return true;
        }
        else{
            return false;
        }
    } 
}