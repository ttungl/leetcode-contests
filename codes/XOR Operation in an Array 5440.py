# XOR Operation in an Array 5440.

# Given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

 

# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.
# Example 2:

# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
# Example 3:

# Input: n = 1, start = 7
# Output: 7
# Example 4:

# Input: n = 10, start = 5
# Output: 2
 

# Constraints:

# 1 <= n <= 1000
# 0 <= start <= 1000
# n == nums.length


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
    	# sol 1:
    	# time O(n) space O(n)
        res = 0
        nums = []
        for i in range(n):
            nums.append(start+2*i)
        for i in nums:
            res^=i
        return res

        # sol 2: 
        # time O(n) space O(1)
        res = 0
        for i in range(n):
            res ^= start+2*i 
        return res