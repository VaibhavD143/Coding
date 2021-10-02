class Leet_simplify_path {
    public String simplifyPath(String path) {
        Stack<String> ss = new Stack<>();
        
        for (String s : path.split("/")) {
            if (s.equals(".") || s.equals("")) {
                continue;
            }
            
            if (s.equals("..")) {
                if (!ss.empty()) {
                    ss.pop();
                }
            }
            else {
                ss.push(s);
            }
        }
        
        return '/' + String.join("/", ss);
    }
}