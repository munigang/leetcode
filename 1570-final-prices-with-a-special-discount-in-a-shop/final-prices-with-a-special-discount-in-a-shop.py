class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        lst=[]
        d=0
        for i in range(0,n):
            for j in range(i+1,n):
                if prices[j]<=prices[i]:
                    d=prices[i]-prices[j]
                    lst.append(d)
                    break
            else:
                lst.append(prices[i])
        return lst

        