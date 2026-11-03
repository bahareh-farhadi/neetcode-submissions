class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_count=0
        ten_count=0
        twenty_count=0
        total=0
        for i in range(len(bills)):
            need=bills[i]-5
            total+=bills[i]
            if bills[i]==5:
                five_count+=1
            elif bills[i]==10:
                ten_count+=1
            elif bills[i]==20:
                twenty_count+=1
            if need>total:
                return False
            else:
                if need==5:
                    if five_count==0:
                        return False
                    else:
                        five_count-=1
                elif need==10:
                    # we should use 10 dollar bills, if not then use 2 5's since we neeed 5's for 15 which makes 5 more versatile
                    if ten_count>0:
                        ten_count-=1
                    else:
                        if five_count>=2:
                            five_count-=2
                        else:
                            return False
                elif need==15:
                    if ten_count>0:
                        ten_count-=1
                        if five_count>0:
                            five_count-=1
                        else:
                            return False
                    else:
                        if five_count>=3:
                            five_count-=3
                        else:
                            return False
        return True
    

        