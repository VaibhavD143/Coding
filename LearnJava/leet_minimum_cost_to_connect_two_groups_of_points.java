package codes;

import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;


public class leet_minimum_cost_to_connect_two_groups_of_points {
    class Pair{
        int ind;
        int mask;
        public Pair(int ind,int mask){
            this.ind = ind;
            this.mask = mask;
        }
        @Override
        public int hashCode() {
            return this.ind ^ this.mask;
        }
    
        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null)
                return false;
            if (getClass() != obj.getClass())
                return false;
            Pair other = (Pair) obj;
            if (ind != other.ind)
                return false;
            if (mask != other.mask)
                return false;
            return true;
        }

    }
    private int[] min_cost;
    private Map<Pair,Integer> ha = new HashMap<>();
    public int connectTwoGroups(List<List<Integer>> cost) {
        
        min_cost = new int[cost.get(0).size()];
        System.out.println(cost.toString());
        for(int j=0;j<cost.get(0).size();j++){
            int mn = Integer.MAX_VALUE;
            for(int i=0;i<cost.size();i++){
                mn = Math.min(mn,cost.get(i).get(j));
            }
            min_cost[j] = mn;
        }
        System.out.println(Arrays.toString(min_cost));
        return fun(0,0,cost);
    }

    public int fun(int ind1,int m2,List<List<Integer>> cost){
        
        if(ha.containsKey(new Pair(ind1,m2))){
            return ha.get(new Pair(ind1,m2));
        }

        if(ind1 != cost.size()){
            int c= Integer.MAX_VALUE;
            for(int j=0;j<cost.get(0).size();j++){
                c = Math.min(c,cost.get(ind1).get(j)+fun(ind1+1,m2|1<<j,cost));
            }
            ha.put(new Pair(ind1,m2),c);
            return c;
        }
        int c=0;
        for(int j=0;j<cost.get(0).size();j++){
            if((m2&1<<j) ==0){
                c+=min_cost[j];
            }
        }
        ha.put(new Pair(ind1,m2),c);
        return c;
    }
    public void run(){
        Scanner sc = new Scanner(System.in);
        List<List<Integer>> cost = new ArrayList<>();
        while(sc.hasNextLine()){
            ArrayList<Integer> row= new ArrayList<>();
            for(String s:sc.nextLine().split(" ")){
                row.add(Integer.parseInt(s));
            }
            cost.add(row);
        }
        System.out.println(this.connectTwoGroups(cost));
    }
}