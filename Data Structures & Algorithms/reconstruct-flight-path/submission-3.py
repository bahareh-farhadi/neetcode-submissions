# the idea is that we don't pop from stack right away, we only pop from stack if that city has no route to other cities, otherwise we add cities one by one to stack. 
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ad_list=dict()
        for t in tickets:
            if t[0] in ad_list:
                ad_list[t[0]].append(t[1])
            else:
                ad_list[t[0]]=[t[1]]
        for key in ad_list:
            ad_list[key].sort(reverse=True)
        path=list()
        stack=list()
        stack.append("JFK")
        while len(stack)>0:
            city=stack[-1]
            if city in ad_list:
                stack.append(ad_list[city].pop())
                if len(ad_list[city])==0:
                    del ad_list[city]
            else:
                path.append(city)
                stack.pop()
        path.reverse()
        return path

        
        