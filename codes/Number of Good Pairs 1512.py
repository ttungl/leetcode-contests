# Number of Good Pairs 1512. 

# Given an array of integers nums.

# A pair (i,j) is called good if nums[i] == nums[j] and i < j.

# Return the number of good pairs.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # sol 1:
        # time O(n(n-1)) space O(1)
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    res+=1
        return res
    
        # sol 2: hashmap
        # time O(n) space O(n)
        res = 0
        d = collections.defaultdict(int)
        for i, v in enumerate(nums):
            d[v]+=1
        for i in d:
            n = d[i]
            res += (n*(n-1))//2
        return res
    
        # sol 3:
        return sum([(n*(n-1))//2 for _,n in collections.Counter(nums).items()])
        
        
        