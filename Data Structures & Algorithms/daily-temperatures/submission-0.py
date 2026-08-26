class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=list()
        res=list()
        for t in temperatures:
            res.append(0)
        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append((temperatures[i], i))
            else:
                while len(stack)>0 and stack[-1][0]<temperatures[i]:
                    res[stack[-1][1]]=i-stack[-1][1]
                    stack.pop()
                stack.append((temperatures[i], i))
        return res
        
        