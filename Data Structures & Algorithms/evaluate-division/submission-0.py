class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ad_list=dict()
        for i in range(len(equations)):
            if equations[i][0] in ad_list:
                ad_list[equations[i][0]].append((equations[i][1], values[i]))
            else:
                ad_list[equations[i][0]]=[(equations[i][1], values[i])]
            
            if equations[i][1] in ad_list:
                ad_list[equations[i][1]].append((equations[i][0], 1/values[i]))
            else:
                ad_list[equations[i][1]]=[(equations[i][0], 1/values[i])]
        
        res=list()
        calculations=dict()
        for q in queries:
            first_char=q[0]
            second_char=q[1]
            if first_char not in ad_list or second_char not in ad_list:
                res.append(-1)
                continue
            if first_char in calculations:
                found=False
                for t in calculations[first_char]:
                    if t[0]==second_char:
                        found=True
                        res.append(t[1])
                        break
                if found==False:
                    res.append(-1)
                continue
            
            stack=list()
            stack.append((first_char, 1))
            visited=set()
            while len(stack)>0:
                elem=stack.pop()
                char=elem[0]
                num=elem[1]
                if first_char not in calculations:
                    calculations[first_char]=set()
                calculations[first_char].add((char, num))
                visited.add(char)
                if char in ad_list:
                    for item in ad_list[char]:
                        next_char=item[0]
                        next_num=item[1]
                        if next_char not in visited:
                            stack.append((next_char, num*next_num))
            found=False
            for t in calculations[first_char]:
                if t[0]==second_char:
                    found=True
                    res.append(t[1])
                    break
            if found==False:
                res.append(-1) 
        return res
            


                        
            

            

        