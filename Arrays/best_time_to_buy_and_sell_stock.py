def stock_purchase(prices):
    l,r=0,1
    max_profit=0
    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            max_profit=max(profit,max_profit)
        else:
            l=r
        r+=1
    return max_profit
print(stock_purchase([1,2,3,4,5]))