import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Pop the character with the highest count. If the last two characters in the result match this character, try using the second-highest instead.
        max_heap=list()
        if a>0:
            heapq.heappush(max_heap, [-a, "a"])
        if b>0:
            heapq.heappush(max_heap, [-b, "b"])
        if c>0:
            heapq.heappush(max_heap, [-c, "c"])
        res=""
        while len(max_heap)>0:
            most_freq=heapq.heappop(max_heap)
            if len(res)>=2 and res[-1]==res[-2] and res[-1]==most_freq[1] and res[-2]==most_freq[1]:
                # use the second most frequent
                if len(max_heap)>0:
                    second_most_freq=heapq.heappop(max_heap)
                    res+=second_most_freq[1]
                    second_most_freq[0]=-(abs(second_most_freq[0])-1)
                    if second_most_freq[0]!=0:
                        heapq.heappush(max_heap, [second_most_freq[0], second_most_freq[1]])
                    heapq.heappush(max_heap, [most_freq[0], most_freq[1]])
                else:
                    break
            else:
                res+=most_freq[1]
                most_freq[0]=-(abs(most_freq[0])-1)
                if most_freq[0]!=0:
                    heapq.heappush(max_heap, [most_freq[0], most_freq[1]])
        return res
                

        