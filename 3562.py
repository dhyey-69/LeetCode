# 3562. Maximum Profit from Trading Stocks with Discounts
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer n, representing the number of employees in a company. Each employee is assigned a unique ID from 1 to n, and employee 1 is the CEO. You are given two 1-based integer arrays, present and future, each of length n, where:

# present[i] represents the current price at which the ith employee can buy a stock today.
# future[i] represents the expected price at which the ith employee can sell the stock tomorrow.
# The company's hierarchy is represented by a 2D integer array hierarchy, where hierarchy[i] = [ui, vi] means that employee ui is the direct boss of employee vi.

# Additionally, you have an integer budget representing the total funds available for investment.

# However, the company has a discount policy: if an employee's direct boss purchases their own stock, then the employee can buy their stock at half the original price (floor(present[v] / 2)).

# Return the maximum profit that can be achieved without exceeding the given budget.

# Note:

# You may buy each stock at most once.
# You cannot use any profit earned from future stock prices to fund additional investments and must buy only from budget.
 

# Example 1:

# Input: n = 2, present = [1,2], future = [4,3], hierarchy = [[1,2]], budget = 3

# Output: 5

# Explanation:



# Employee 1 buys the stock at price 1 and earns a profit of 4 - 1 = 3.
# Since Employee 1 is the direct boss of Employee 2, Employee 2 gets a discounted price of floor(2 / 2) = 1.
# Employee 2 buys the stock at price 1 and earns a profit of 3 - 1 = 2.
# The total buying cost is 1 + 1 = 2 <= budget. Thus, the maximum total profit achieved is 3 + 2 = 5.
# Example 2:

# Input: n = 2, present = [3,4], future = [5,8], hierarchy = [[1,2]], budget = 4

# Output: 4

# Explanation:



# Employee 2 buys the stock at price 4 and earns a profit of 8 - 4 = 4.
# Since both employees cannot buy together, the maximum profit is 4.
# Example 3:

# Input: n = 3, present = [4,6,8], future = [7,9,11], hierarchy = [[1,2],[1,3]], budget = 10

# Output: 10

# Explanation:



# Employee 1 buys the stock at price 4 and earns a profit of 7 - 4 = 3.
# Employee 3 would get a discounted price of floor(8 / 2) = 4 and earns a profit of 11 - 4 = 7.
# Employee 1 and Employee 3 buy their stocks at a total cost of 4 + 4 = 8 <= budget. Thus, the maximum total profit achieved is 3 + 7 = 10.
# Example 4:

# Input: n = 3, present = [5,2,3], future = [8,5,6], hierarchy = [[1,2],[2,3]], budget = 7

# Output: 12

# Explanation:



# Employee 1 buys the stock at price 5 and earns a profit of 8 - 5 = 3.
# Employee 2 would get a discounted price of floor(2 / 2) = 1 and earns a profit of 5 - 1 = 4.
# Employee 3 would get a discounted price of floor(3 / 2) = 1 and earns a profit of 6 - 1 = 5.
# The total cost becomes 5 + 1 + 1 = 7 <= budget. Thus, the maximum total profit achieved is 3 + 4 + 5 = 12.
 

# Constraints:

# 1 <= n <= 160
# present.length, future.length == n
# 1 <= present[i], future[i] <= 50
# hierarchy.length == n - 1
# hierarchy[i] == [ui, vi]
# 1 <= ui, vi <= n
# ui != vi
# 1 <= budget <= 160
# There are no duplicate edges.
# Employee 1 is the direct or indirect boss of every employee.
# The input graph hierarchy is guaranteed to have no cycles.

n = 2
p = [1,2]
f = [4,3]
h = [[1,2]]
b = 3

# n = 2
# p = [3,4]
# f = [5,8]
# h = [[1,2]]
# b = 4

# n = 3
# p = [4,6,8]
# f = [7,9,11]
# h = [[1,2],[1,3]]
# b = 10

# n = 3
# p = [5,2,3]
# f = [8,5,6]
# h = [[1,2],[2,3]]
# b = 7

def xyz(n,present,future,hierarchy,budget):
    N = n
    NEG = -10**9

    profit = [[0, 0] for _ in range(N)]
    for i in range(N):
        profit[i][0] = future[i] - present[i]
        profit[i][1] = future[i] - (present[i] // 2)

    children = [[] for _ in range(N)]
    for u, v in hierarchy:
        children[u - 1].append(v - 1)

    dp = [[[[NEG] * (budget + 1) for _ in range(2)]
            for _ in range(2)] for _ in range(N)]

    vis = [[[False] * 2 for _ in range(2)] for _ in range(N)]

    def dfs(node, bossBuy, buy):
        if vis[node][bossBuy][buy]:
            return
        vis[node][bossBuy][buy] = True

        cache = dp[node][bossBuy][buy]
        for i in range(budget + 1):
            cache[i] = NEG

        cost = 0
        if buy:
            cost = present[node] // 2 if bossBuy else present[node]

        if cost <= budget:
            cache[cost] = profit[node][bossBuy] if buy else 0

        cur = cache[:]

        for child in children[node]:
            dfs(child, buy, 1)
            dfs(child, 0, 0)

            take = dp[child][buy][1]
            skip = dp[child][0][0]

            merged = [NEG] * (budget + 1)

            for b in range(budget + 1):
                if cur[b] == NEG:
                    continue
                cb = cur[b]
                for x in range(budget - b + 1):
                    best = take[x] if take[x] > skip[x] else skip[x]
                    if best != NEG:
                        val = cb + best
                        if val > merged[b + x]:
                            merged[b + x] = val

            cur = merged

        dp[node][bossBuy][buy] = cur[:]

    dfs(0, 0, 0)
    dfs(0, 0, 1)

    ans = 0
    for b in range(budget + 1):
        if dp[0][0][0][b] > ans:
            ans = dp[0][0][0][b]
        if dp[0][0][1][b] > ans:
            ans = dp[0][0][1][b]

    return ans

print(xyz(n,p,f,h,b))