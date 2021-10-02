package codes;

class leet_maximum_profit_of_operating_a_centennial_wheel {
    public int minOperationsMaxProfit(int[] cust, int board, int run) {
        int rem=0;
        int ans=0,cnt=-1;
        int cur=0,profit=0;
        int i=0;
        while(rem>0 || i<cust.length){
            if(i<cust.length){
                rem+=cust[i];
            }
            
            int bd = Math.min(4,rem);
            rem -= bd;
            profit += bd*board-run;
            if(profit>ans){
                ans=profit;
                cnt=i+1;
            }
            i++;
        }
        return cnt;
    }

    public void run(){
        System.out.println(this.minOperationsMaxProfit(new int[]{3,4,0,5,1}, 1, 92));
    }
}