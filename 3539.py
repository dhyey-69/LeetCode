# 3539. Find Sum of Array Product of Magical Sequences
# Hard
# Topics
# premium lock icon
# Companies
# Hint
# You are given two integers, m and k, and an integer array nums.

# A sequence of integers seq is called magical if:
# seq has a size of m.
# 0 <= seq[i] < nums.length
# The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
# The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).

# Return the sum of the array products for all valid magical sequences.

# Since the answer may be large, return it modulo 109 + 7.

# A set bit refers to a bit in the binary representation of a number that has a value of 1.

 

# Example 1:

# Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]

# Output: 991600007

# Explanation:

# All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.

# Example 2:

# Input: m = 2, k = 2, nums = [5,4,3,2,1]

# Output: 170

# Explanation:

# The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].

# Example 3:

# Input: m = 1, k = 1, nums = [28]

# Output: 28

# Explanation:

# The only magical sequence is [0].

 

# Constraints:

# 1 <= k <= m <= 30
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 108


m = 5
k = 5
n = [1,10,100,10000,1000000]

m = 2
k = 2
n = [5,4,3,2,1]

m = 1
k = 1
n = [28]

MOD = 10**9 + 7
from functools import lru_cache
import math

def xyz(m,k,nums):
    @lru_cache(None)
    def dfs(remaining, odd_needed, index, carry):
        if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
            return 0
        if remaining == 0:
            return 1 if odd_needed == carry.bit_count() else 0
        if index >= len(nums):
            return 0
        
        ans = 0
        for take in range(remaining + 1):
            ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
            new_carry = carry + take
            ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
            ans %= MOD
        return ans
    
    return dfs(m, k, 0, 0)

print(xyz(m,k,n))