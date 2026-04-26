# Stock Buy and Sell

def stock_pro(prices):
    min_price = float('inf')
    max_pro = 0
    n = len(prices)

    for i in range(n):
        min_price = min(min_price, prices[i])
        max_pro = max(max_pro, prices[i] - min_price)

    return max_pro

prices = [7,2,1,5,6,4,8]
print(stock_pro(prices))

# Time Complexity (TC): O(n)
# Space Complexity (SC): O(1)