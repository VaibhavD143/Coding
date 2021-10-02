
class leet_crawler_log_folder {
    public int minOperations(String[] logs) {
        int cnt = 0;
        for(String s:logs){
            if(s.equals("../")){
                cnt = Math.max(cnt-1,0);
            }
            else if(s.equals("./")){
            }
            else{
                cnt+=1;
            }
        }
        return cnt;
        
    }

    public void run(){
        System.out.println(this.minOperations(new String[]{"d1/","d2/","../","d21/","./"}));
    }
}
