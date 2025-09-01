# 1792. Maximum Average Pass Ratio
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
# Output: 0.78333
# Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
# Example 2:

# Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
# Output: 0.53485
 

# Constraints:

# 1 <= classes.length <= 105
# classes[i].length == 2
# 1 <= passi <= totali <= 105
# 1 <= extraStudents <= 105


c = [[1,2],[3,5],[2,2]]
exs = 2

# c = [[2,4],[3,9],[4,5],[2,10]]
# exs = 4

def xyz(classes,extraStudents):
    def gain(p, t):
        return (p + 1) / (t + 1) - p / t
    
    def heapify_down(i):
        n = len(heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and heap[left][0] > heap[largest][0]:
                largest = left
            if right < n and heap[right][0] > heap[largest][0]:
                largest = right
            if largest == i:
                break
            heap[i], heap[largest] = heap[largest], heap[i]
            i = largest
    
    def heapify_up(i):
        while i > 0:
            parent = (i - 1) // 2
            if heap[i][0] > heap[parent][0]:
                heap[i], heap[parent] = heap[parent], heap[i]
                i = parent
            else:
                break
    
    heap = []
    for p, t in classes:
        heap.append((gain(p, t), p, t))
    for i in reversed(range(len(heap)//2)):
        heapify_down(i)
    
    for _ in range(extraStudents):
        g, p, t = heap[0]
        p, t = p + 1, t + 1
        heap[0] = (gain(p, t), p, t)
        heapify_down(0)
    
    total = 0
    for _, p, t in heap:
        total += p / t
    return total / len(classes)


print(xyz(c,exs))