class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # the idea is to do the multiplications in-place, basically we will create a final array of length (n+m), we will reverse num1 and num2 and keep track of a carry and res[i+j] = num1[i] * num2[j] + carry would be the result, we will have to reverse the final string and get rid of the leaging zeros
        res = [0] * (len(num1) + len(num2))
        reversed_num1 = num1[::-1]
        reversed_num2 = num2[::-1]
        for i in range(len(reversed_num1)):
            for j in range(len(reversed_num2)):
                curr_sum = int(reversed_num1[i]) * int(reversed_num2[j])
                res[i+j]+= curr_sum
                res[i+j+1] += res[i+j] // 10
                res[i+j] = res[i+j] % 10
        res.reverse()
        start = 0
        for i in range(len(res)):
            if res[i] != 0:
                break
            start+=1
        if start < len(res):
            final = ""
            for i in range(start, len(res)):
                final+=str(res[i])
            return final
        else:
            return "0"
                   
        