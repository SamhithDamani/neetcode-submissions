class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find min and index(first occurence of min), from that index find max and index -- misses cases in[2,10,1,1,1,]
        profits=[0 for i in range(len(prices))]
        for i in range(len(prices)-1):
            max_profit=0
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>max_profit:
                    max_profit=prices[j]-prices[i]
            profits[i]=max_profit
        return max(profits)
        

             
        