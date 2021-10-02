class leet_maximum_number_of_achievable_transfer_request {
    public int maximumRequests(int n, int[][] req) {
        int mask = (1<<req.length);
        int ans=0;
        for(int i=0;i<mask;i++){
            int cnt = count(i);
            if(cnt>ans && isPossible(i,n,req)){
                ans = cnt;
            }
        }
        // System.out.println(count(53));
        // System.out.println(isPossible(53,req));
        return ans;
        
    }
    
    public boolean isPossible(int mask,int n,int[][] req){
        int[] in = new int[n];
        
        for(int i=0;i<req.length;i++){
            if((mask&(1<<i))!=0){
                in[req[i][1]]++;
                in[req[i][0]]--;
            }
            // System.out.println(Arrays.toString(in));
        }
        for(int i:in){
            if(i!=0){
                return false;
            }
        }
        return true;
    }
    
    public int count(int i){
        int cnt = 0;
        while(i>0){
            i=i&(i-1);
            cnt++;
        }
        return cnt;
    }
}