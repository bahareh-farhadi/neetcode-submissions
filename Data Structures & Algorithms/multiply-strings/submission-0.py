class Solution:
    def sum_helper(self, num1, num2):
        res = list()
        carry = 0
        curr_sum = 0
        i = len(num1) - 1
        j = len(num2) - 1
        while i >= 0 and j >= 0:
            curr_sum = int(num1[i]) + int(num2[j]) + carry
            curr_digit = str(curr_sum % 10)
            res.append(curr_digit)
            carry = curr_sum // 10
            i-=1
            j-=1
        while i >= 0:
            curr_sum = int(num1[i]) + carry
            curr_digit = str(curr_sum % 10)
            res.append(curr_digit)
            carry = curr_sum // 10
            i-=1
        while j >= 0:
            curr_sum = int(num2[j]) + carry
            curr_digit = str(curr_sum % 10)
            res.append(curr_digit)
            carry = curr_sum // 10
            j-=1
        if carry > 0:
            curr_digit = str(carry)
            res.append(curr_digit)
        res.reverse()
        return res

    def multiply(self, num1: str, num2: str) -> str:
        res = ["0"]
        k = 0
        for i in range(len(num1)-1, -1, -1):
            curr_num = list()
            
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                curr_sum = int(num1[i]) * int(num2[j]) + carry
                curr_num.append(str(curr_sum % 10))
                carry = curr_sum // 10
            if carry > 0:
                curr_num.append(str(carry))
            curr_num.reverse()
            for m in range(k):
                curr_num.append("0")
            res = self.sum_helper(curr_num, res)
            k+=1
        # remove leading 0's
        start = 0
        for i in range(len(res)):
            if res[i] != "0":
                break
            start+=1
        if start < len(res):
            return "".join(map(str, res[start:]))
        else:
            return "0"




        
        