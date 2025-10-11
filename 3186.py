# 3186. Maximum Total Damage With Spell Casting
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# A magician has various spells.

# You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

# It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

# Each spell can be cast only once.

# Return the maximum possible total damage that a magician can cast.

 

# Example 1:

# Input: power = [1,1,3,4]

# Output: 6

# Explanation:

# The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

# Example 2:

# Input: power = [7,1,6,6]

# Output: 13

# Explanation:

# The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

# Constraints:

# 1 <= power.length <= 105
# 1 <= power[i] <= 109


p = [1,1,3,4]
p = [7,1,6,6]

def xyz(power):
    damage_map = {}
    for p in power:
        damage_map[p] = damage_map.get(p, 0) + p

    unique = sorted(damage_map.keys())
    total = [damage_map[x] for x in unique]
    n = len(unique)

    dp = [0] * n
    j = -1

    for i in range(n):
        while j + 1 < i and unique[j + 1] < unique[i] - 2:
            j += 1

        include = total[i] + (dp[j] if j >= 0 else 0)
        exclude = dp[i - 1] if i > 0 else 0
        dp[i] = max(include, exclude)

    return dp[-1]

print(xyz(p))