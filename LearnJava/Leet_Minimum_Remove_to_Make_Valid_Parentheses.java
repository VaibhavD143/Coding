class Leet_Minimum_Remove_to_Make_Valid_Parentheses {
    public String minRemoveToMakeValid(String s) {
        char[] str = s.toCharArray();
        int diff = 0;
        for (int i = 0; i < str.length; i++) {
            if (str[i] == '(') {
                diff++;
            }
            else if (str[i] == ')') {
                if (diff > 0) {
                    diff--;
                }
                else {
                    str[i] = '?';
                }
            } 
                
        }
        int i = str.length-1;
        while (diff > 0) {
            if (str[i] == '(') {
                str[i] = '?';
                diff--;
            }
            i--;
        }
        StringBuilder sb = new StringBuilder();
        for (char c : str) {
            if (c != '?') {
                sb.append(c);
            }
        }
        return sb.toString();
    }
}