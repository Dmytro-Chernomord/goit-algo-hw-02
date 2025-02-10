def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin

    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin == -1:
            return {}
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result


# Testing
amount = 167
print("Greedy Algorithm:", find_coins_greedy(amount))
print("Dynamic Programming Algorithm:", find_min_coins(amount))
