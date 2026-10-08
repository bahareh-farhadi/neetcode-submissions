class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=list()
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>=0 and j>=0:
            first_num=int(a[i])
            second_num=int(b[j])
            curr=first_num+second_num+carry
            if curr==0:
                res.append("0")
                carry=0
            elif curr==1:
                res.append("1")
                carry=0
            else:
                res.append(str(curr-2))
                carry=1
            i-=1
            j-=1
        while i>=0:
            first_num=int(a[i])
            curr=first_num+carry
            if curr==0:
                res.append("0")
                carry=0
            elif curr==1:
                res.append("1")
                carry=0
            else:
                res.append(str(curr-2))
                carry=1
            i-=1
        while j>=0:
            first_num=int(b[j])
            curr=first_num+carry
            if curr==0:
                res.append("0")
                carry=0
            elif curr==1:
                res.append("1")
                carry=0
            else:
                res.append(str(curr-2))
                carry=1
            j-=1
        print(carry)
        if carry==1:
            res.append("1")
        
        return "".join(res[::-1])

        