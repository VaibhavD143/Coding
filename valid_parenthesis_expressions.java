// Program to find number of valid expressions possible from given (n) number of paranthesis
// https://www.geeksforgeeks.org/program-nth-catalan-number/

import java.util.ArrayList;
import java.util.Collections;

class valid_parenthesis_expressions{
    // ArrayList<Integer> count = new ArrayList<>();
    int[][] count;
    public void _initialise(int n) {
        // this.count.add(1);
        count = new int[1+n][1+n];
        // Collections.sort(count);
        for (int i = 0; i < n+1; i++) {
            for (int j = 0; j < n+1; j++) {
                this.count[i][j] = -1;
            }
        }
        this.count[0][0] = 1;
    }

    public int fun2(int open,int close){
        System.out.println("----------");
        System.out.println(open+"----"+close);
        if(open>close){
            return 0;
        }
        if(this.count[open][close] != -1){
            return this.count[open][close];
        }
        if(open == 0){
            this.count[open][close] = fun2(open,close-1);
            return this.count[open][close];
        }
        this.count[open][close] = fun2(open,close-1)+fun2(open-1,close);
        return this.count[open][close];
    }

    void run(){
        int n = 3;        
        _initialise(n);
        System.out.println(fun2(n,n));
        System.out.println(this.count[n]);
    }

    public static void main(String[] args) {
        // int n = 3;
        // valid_parenthesis_expressions obj = new valid_parenthesis_expressions();
        // obj._initialise(n);
        // System.out.println(obj.fun(n,n));
        // System.out.println(obj.count);
        new valid_parenthesis_expressions().run();

    }
}