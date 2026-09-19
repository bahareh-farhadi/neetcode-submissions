import heapq
import math
class Solution:
    def reorganizeString(self, s: str) -> str:
        # the idea is to use a max heap to store the frequency of the characters, e.g. (freq, char), then each time we pop the 2 most frequent elements, we add them to the result, then we decremenet their frequencies and add them back to the max heap
        seen=dict()
        for char in s:
            if char in seen:
                seen[char]+=1
            else:
                seen[char]=1
        max_heap=list()
        for char, freq in seen.items():
            heapq.heappush(max_heap, [-freq, char])
        if abs(max_heap[0][0])>math.ceil(len(s)/2):
            return "" #impossible
        res=""
        while len(max_heap)>0:
            most_freq=heapq.heappop(max_heap)
            if len(max_heap)>0:
                second_most_freq=heapq.heappop(max_heap)
                res+=most_freq[1]
                res+=second_most_freq[1]
                most_freq[0]=-(abs(most_freq[0])-1)
                if most_freq[0]!=0:
                    heapq.heappush(max_heap, most_freq)
                second_most_freq[0]=-(abs(second_most_freq[0])-1)
                if second_most_freq[0]!=0:
                    heapq.heappush(max_heap, second_most_freq)
            else:
                res+=most_freq[1]
        return res

        