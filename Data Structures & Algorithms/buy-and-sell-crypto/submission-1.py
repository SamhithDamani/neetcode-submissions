class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find min and index(first occurence of min), from that index find max and index -- misses cases in[2,10,1,1,1,]
        maxp=0
        minBuy=prices[0]
        for i in prices:
            maxp=max(maxp,i-minBuy)
            minBuy=min(minBuy,i)
        return maxp
        

             
        