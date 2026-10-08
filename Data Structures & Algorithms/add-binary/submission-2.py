class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>=0 and j>=0:
            first_num=int(a[i])
            second_num=int(b[j])
            curr=first_num+second_num+carry
            if curr==0:
                res="0"+res
                carry=0
            elif curr==1:
                res="1"+res
                carry=0
            else:
                res=str(curr-2)+res
                carry=1
            i-=1
            j-=1
        while i>=0:
            first_num=int(a[i])
            curr=first_num+carry
            if curr==0:
                res="0"+res
                carry=0
            elif curr==1:
                res="1"+res
                carry=0
            else:
                res=str(curr-2)+res
                carry=1
            i-=1
        while j>=0:
            first_num=int(b[j])
            curr=first_num+carry
            if curr==0:
                res="0"+res
                carry=0
            elif curr==1:
                res="1"+res
                carry=0
            else:
                res=str(curr-2)+res
                carry=1
            j-=1
        print(carry)
        if carry==1:
            res="1"+res
        return res

        