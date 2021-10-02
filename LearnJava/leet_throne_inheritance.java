import java.util.*;

class leet_throne_inheritance {
    private Map<String, LinkedList<String>> ha;
    private Set<String> dead;
    private String king;
    public void ThroneInheritance(String kingName) {
        this.ha = new HashMap<>();
        this.ha.put(kingName,new LinkedList<>());
        this.dead = new HashSet<>();
        this.king = kingName;
    }
    
    public void birth(String parentName, String childName) {
        this.ha.get(parentName).add(childName);
        this.ha.put(childName,new LinkedList<>());
    }
    
    public void death(String name) {
        this.dead.add(name);
    }
    
    public List<String> getInheritanceOrder() {
        List<String> res = new LinkedList<>();
        dfs(this.king,res);
        // LinkedList<String> ss = new LinkedList<>();
        // ss.add(this.king);
        // while(ss.size()!=0){
        //     String name = ss.removeLast();
        //     if(!this.dead.contains(name)){
        //         res.add(name);
        //     }
        //     ss.addAll(this.ha.get(name));
        // }
        return res;
    }
    
    public void dfs(String node,List<String> res){
        if(!this.dead.contains(node)){
            res.add(node);
        }
        for(String v:this.ha.get(node)){
            dfs(v,res);
        }
    }
}
