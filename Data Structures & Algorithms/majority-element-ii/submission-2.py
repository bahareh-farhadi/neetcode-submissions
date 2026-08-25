class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1=None
        count1=0
        num2=None
        count2=0
        for num in nums:
            if num1!=None and num==num1:
                count1+=1
            elif num2!=None and num==num2:
                count2+=1
            elif count1==0:
                num1=num
                count1=1
            elif count2==0:
                num2=num
                count2=1
            else:
                count1-=1
                count2-=1
        # verify , count actual occurences
        count1=0
        count2=0
        for num in nums:
            if num1!=None and num==num1:
                count1+=1
            elif num2!=None and num==num2:
                count2+=1
        res=list()
        if num1!=None and count1>(len(nums)/3):
            res.append(num1)
        if num2!=None and count2>(len(nums)/3):
            res.append(num2)
        return res
        