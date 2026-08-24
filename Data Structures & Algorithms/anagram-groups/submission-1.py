class Solution:
    def create_key(self, string):
        key=list()
        for i in range(26):
            key.append(0)
        for i in range(len(string)):
            key[ord(string[i])-ord('a')]+=1
        key = ' '.join(map(str, key))
        return key
            
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=dict()
        for string in strs:
            key=self.create_key(string)
            if key in groups:
                groups[key].append(string)
            else:
                groups[key]=[string]
        res=list()
        for key, val in groups.items():
            res.append(val)
        return res
        