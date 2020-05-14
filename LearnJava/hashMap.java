import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

import jdk.nashorn.internal.runtime.arrays.ArrayLikeIterator;

class hashMap{
    public static void main(String[] args) {
        HashMap<String,Integer> myMap = new HashMap<>();
        myMap.put("Hey",1);
        myMap.put("Ther", 2);
        myMap.put("Alive?", 3);
        System.out.println(myMap.get("Hey"));
        System.out.println(myMap.entrySet().getClass().getName());
        System.out.println(myMap.size());
        
        for(Map.Entry elem : myMap.entrySet()){
            System.out.println(elem.getKey()+" "+elem.getValue());
            // elem.setValue(value);
        }
        Iterator<Map.Entry<String,Integer>> it = myMap.entrySet().iterator();
        while(it.hasNext()){
            Map.Entry<String,Integer> i = it.next();
            System.out.println(i.getKey());
        }

        ArrayList<Integer> a = new ArrayList<>();
        a.add(4);
        a.add(4);
        a.add(4);
        myMap.replace("Hey", 5);
        System.out.println(myMap);
        myMap.remove("Hey");
        System.out.println(myMap);
        
    }
}