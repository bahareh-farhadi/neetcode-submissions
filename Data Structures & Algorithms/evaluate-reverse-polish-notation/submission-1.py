class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=list()
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            
            else:
                arg2=stack.pop()
                arg1=stack.pop()
                if token=="+":
                    res=arg1+arg2
                elif token=="-":
                    res=arg1-arg2
                elif token=="*":
                    res=arg1*arg2
                elif token=="/":
                    res=int(arg1/arg2)
                stack.append(res)
                
        return stack.pop()


        