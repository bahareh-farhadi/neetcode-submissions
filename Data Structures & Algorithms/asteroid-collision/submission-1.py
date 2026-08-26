class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=list()
        for ast in asteroids:
            if len(stack)>0:
                if stack[-1]<0 and ast<0:
                    stack.append(ast)
                elif stack[-1]>0 and ast>0:
                    stack.append(ast)
                elif stack[-1]<0 and ast>0:
                    # no collision
                    stack.append(ast)
                else:
                    add=False
                    while len(stack)>0 and stack[-1]>0 and ast<0:
                        if stack[-1]==abs(ast):
                            stack.pop()
                            add=False
                            break
                        elif stack[-1]<abs(ast):
                            stack.pop()
                            add=True
                        elif stack[-1]>abs(ast):
                            add=False
                            break
                    if add==True:
                        stack.append(ast)
                        
            else:
                stack.append(ast)
        return stack
        