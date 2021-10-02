import java.util.*;
class Solution {
    public static int[] findOrder(int num, int[][] pre) {
        int res[] = new int[num];
        int ind[] = new int[num];
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<num;i++){
            graph.add(new ArrayList<Integer>());
        }
        for(int i=0;i<pre.length;i++){
            graph.get(pre[i][1]).add(pre[i][0]);
            ind[pre[i][0]]++;
        }
        
        Deque<Integer> lst = new ArrayDeque<>();
        for(int i=0;i<ind.length;i++){
            if (ind[i]==0){
                lst.add(i);
            }
        }
        // System.out.println(Arrays.toString(ind));
        int index=0;
        while(lst.peek()!= null){
            res[index] = lst.poll();
            for(int v:graph.get(res[index])){
                ind[v]--;
                if(ind[v] == 0){
                    lst.add(v);
                }
            }
            index++;
        }
        return index == num?res:new int[0];   
    }
    public static void main(String[] args) {
        int[][] pre = {{1,0},{2,0},{3,1},{3,2}};
        int[] res = Solution.findOrder(4,pre);
        System.out.println(Arrays.toString(res));
    }
}