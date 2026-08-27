class Solution:
    def det_new_str(stack):
        res=""
        while len(stack)>0:
            item=stack.pop()
            if isinstance(item, int):
                s=stack.pop()
                for i in range(item):
                    res+=s
            else:
                res+=item
        return res

        
    def decodeString(self, s: str) -> str:
        # the idea is to use 2 stacks
        # the first stack takes care of all elements, once we see a ] we keep popping off elements until we see [. The popped elements get added to the second stack. Then we determine the new string formed by whatever is inside the second stack and add that new string to the first stack and continue.
        s1=list()
        s2=list()
        i=0
        while i<len(s):
            if s[i].isalpha():
                new_string=""
                while i<len(s) and s[i].isalpha():
                    new_string+=s[i]
                    i+=1
                s1.append(new_string)
            elif s[i].isdigit():
                new_num=""
                while i<len(s) and s[i].isdigit():
                    new_num+=s[i]
                    i+=1
                s1.append(int(new_num))
            elif s[i]=="[":
                s1.append(s[i])
                i+=1
            elif s[i]=="]":
                print(f"s1 {s1}")
                while s1[-1]!="[":
                    s2.append(s1.pop())
                s1.pop()
                print(f"s2 before {s2}")
                new_string=Solution.det_new_str(s2)
                print(f"s2 after {s2}")
                s1.append(new_string)
                i+=1
        res=""
        while len(s1)>0:
            s2.append(s1.pop())
        if len(s2)>0:
            res+=Solution.det_new_str(s2)
        return res
            
                
                    
            
        