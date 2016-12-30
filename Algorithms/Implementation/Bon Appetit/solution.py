
if __name__ == '__main__':
    n,k = input().strip().split(' ')
    n,k = [int(n), int(k)]
    prices = [int(x) for x in input().strip().split(' ')]
    cost = int(input())
    
    del prices[k]
    
    perCost = (sum(prices) // 2)
    
    if(perCost == cost):
        print("Bon Appetit")
    else:
        print(cost - perCost)
