class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [part for part in path.split('/') if part != '']
        print(path)
        dirs=["/"]
        for p in path:
            if p==".":
                continue
            elif p=="..":
                if dirs[-1]=="/":
                    continue
                else:
                    dirs.pop()
            else:
                dirs.append(p)
        print(dirs)
        res=""
        for i in range(1, len(dirs)):
            res+=f"/{dirs[i]}"
        if len(res)==0:
            res="/"
        return res
            
        