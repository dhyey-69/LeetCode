# 1733. Minimum Number of People to Teach
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

# Example 1:

# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:

# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

# Constraints:

# 2 <= n <= 500
# languages.length == m
# 1 <= m <= 500
# 1 <= languages[i].length <= n
# 1 <= languages[i][j] <= n
# 1 <= u​​​​​​i < v​​​​​​i <= languages.length
# 1 <= friendships.length <= 500
# All tuples (u​​​​​i, v​​​​​​i) are unique
# languages[i] contains only unique values

n = 2
l = [[1],[2],[1,2]]
f = [[1,2],[1,3],[2,3]]

# n = 3
# l = [[2],[1,3],[1,2],[3]]
# f = [[1,4],[1,2],[3,4],[2,3]]

def xyz(n,languages,friendships):
    user_langs = [set(langs) for langs in languages]
  
    problematic_users = set()
    for u, v in friendships:
        u, v = u - 1, v - 1
        if user_langs[u].isdisjoint(user_langs[v]):
            problematic_users.add(u)
            problematic_users.add(v)
    
    if not problematic_users:
        return 0
    
    min_teach = float("inf")
    for lang in range(1, n + 1):
        need_teach = 0
        for user in problematic_users:
            if lang not in user_langs[user]:
                need_teach += 1
        min_teach = min(min_teach, need_teach)
    
    return min_teach

print(xyz(n,l,f))