# Max Value of Equation 1499. 

# Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

# Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 

# Example 1:

# Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
# Output: 4
# Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
# No other pairs satisfy the condition, so we return the max of 4 and 1.
# Example 2:

# Input: points = [[0,0],[3,0],[9,2]], k = 3
# Output: 3
# Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 

# Constraints:

# 2 <= points.length <= 10^5
# points[i].length == 2
# -10^8 <= points[i][0], points[i][1] <= 10^8
# 0 <= k <= 2 * 10^8
# points[i][0] < points[j][0] for all 1 <= i < j <= points.length
# xi form a strictly increasing sequence.

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # sol 1: priority queue
        # time O(nlogn) space O(n)
        # since xi < xj, yi+yj + xj-xi = yi - xi + (xj+yj).
        # find max value of (yi-xi).
        # to find max value in a sliding window, using priority queue or stack.
        heap = []
        res = float('-inf')
        for x, y in points:
            while heap and heap[0][1] < x - k: # remove if xi < xj - k.
                heapq.heappop(heap)
            if heap: 
                res = max(res, -heap[0][0] + x+y) # update ((yi-xi) + xj+yj)
            heapq.heappush(heap, (-(y-x), x))
        return res
            
        # sol 2:
        # time O(n) space O(n)
        queue = collections.deque()
        res = float('-inf')
        for x,y in points:
            while queue and queue[0][1] < x - k:
                queue.popleft()
            if queue:
                res = max(res, queue[0][0]+x+y)
            while queue and queue[-1][0] <= y-x: 
                queue.pop()
            queue.append((y-x, x))
        return res