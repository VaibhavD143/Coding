import java.util.LinkedList;
import java.util.List;
class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        List<Integer> res = new LinkedList<>();
        int[] ind = new int[n];
        for (List<Integer> edge : edges) {
            ind[edge.get(1)]++;
        }
        for(int i=0;i<n;i++){
            if(ind[i]==0){
                res.add(i);
            }
        }
        return res;
    }
}