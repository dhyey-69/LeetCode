# 3405. Count the Number of Arrays with K Matching Adjacent Elements
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given three integers n, m, k. A good array arr of size n is defined as follows:

# Each element in arr is in the inclusive range [1, m].
# Exactly k indices i (where 1 <= i < n) satisfy the condition arr[i - 1] == arr[i].
# Return the number of good arrays that can be formed.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, m = 2, k = 1

# Output: 4

# Explanation:

# There are 4 good arrays. They are [1, 1, 2], [1, 2, 2], [2, 1, 1] and [2, 2, 1].
# Hence, the answer is 4.
# Example 2:

# Input: n = 4, m = 2, k = 2

# Output: 6

# Explanation:

# The good arrays are [1, 1, 1, 2], [1, 1, 2, 2], [1, 2, 2, 2], [2, 1, 1, 1], [2, 2, 1, 1] and [2, 2, 2, 1].
# Hence, the answer is 6.
# Example 3:

# Input: n = 5, m = 2, k = 0

# Output: 2

# Explanation:

# The good arrays are [1, 2, 1, 2, 1] and [2, 1, 2, 1, 2]. Hence, the answer is 2.
 

# Constraints:

# 1 <= n <= 105
# 1 <= m <= 105
# 0 <= k <= n - 1


n = 3
m = 2
k = 1

n = 4
m = 2
k = 2

n = 5
m = 2
k = 0

MOD = 1_000_000_007

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if k > n - 1:
            return 0
        g = n - k
        if g <= 0:
            return 0
        if not hasattr(self, "_fact") or len(self._fact) < n + 1:
            self._build_fact(n)
        
        comb = self._fact[n-1] * self._inv_fact[g-1] % MOD * self._inv_fact[n-g] % MOD
        color_ways = m * pow(m-1, g-1, MOD) % MOD
        
        return comb * color_ways % MOD
    
    def _build_fact(self, up_to: int):
        fact = [1]*(up_to+1)
        for i in range(1, up_to+1):
            fact[i] = fact[i-1]*i % MOD
        inv_fact = [1]*(up_to+1)
        inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
        for i in range(up_to, 0, -1):
            inv_fact[i-1] = inv_fact[i]*i % MOD
        self._fact = fact
        self._inv_fact = inv_fact