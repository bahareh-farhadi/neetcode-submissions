class Solution:
    # we can mark the start of each element with a # and before that we store the length of the element, e.g.
    # ["Hello","World"] becomes 5#Hello5#World

    def encode(self, strs: List[str]) -> str:
        res=""
        for string in strs:
            res+=str(len(string))
            res+="#"
            res+=string
        return res

    def decode(self, s: str) -> List[str]:
        res=list()
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            i=j+1
            string=s[i:i+length]
            res.append(string)
            i=i+length
        return res

