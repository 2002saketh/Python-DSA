def stock_purchase(arr):
    min_price=arr[0]
    max_profit=0
    for price in arr[1:]:
        profit=price-min_price
        max_profit=max(profit,max_profit)
        min_price=min(min_price,price)
    return max_profit
print(stock_purchase([1,2,3,4,5]))