class Solution:
    def hammingWeight(self, n: int) -> int:
        # num & 1 indicates whether the least significant bit is 1 or not
        # we continue shifting the bits to the right to go over all bits
        num_ones=0
        while n>0:
            lsb=n&1
            if lsb==1:
                num_ones+=1
            n=n>>1
        return num_ones
        