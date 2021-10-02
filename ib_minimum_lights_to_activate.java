public class Solution {
    public int solve(int[] A, int B) {
        for(int i=0;i<A.length;i++){
            if(A[i]==1){
                A[Math.max(0,i-B+1)] = i+B-1; 
            }
            else{
                A[i] = -1;
            }
        }
        int cnt=0,cur=-1,nxt=-1;
        for(int i=0;i<A.length;i++){
            nxt = Math.max(nxt,A[i]);
            if(i>cur){
                if(nxt<i){
                    return -1;
                }
                cnt++;
                cur = nxt;
            }
        }
        return cnt;
    }
}
