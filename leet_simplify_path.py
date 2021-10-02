class Solution:
    def simplifyPath(self, path: str) -> str:
        ss = []
        for s in path.split('/') :
            if s and s != '.' :
                if s == ".." :
                    if ss :
                        ss.pop()
                else :
                    ss.append(s)
        return '/' + '/'.join(ss)
    
                    