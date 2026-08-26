class StockSpanner:
    # we keep track of each element and its span
    # when adding a new price we check the top element, and while its price is less than today's price we add its span to today's span and then we pop if off the stack

    def __init__(self):
        self.stack=list()
        

    def next(self, price: int) -> int:
        span=1
        while len(self.stack)>0 and self.stack[-1][0]<=price:
            span+=self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)