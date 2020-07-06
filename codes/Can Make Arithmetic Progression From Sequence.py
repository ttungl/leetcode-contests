# Can Make Arithmetic Progression From Sequence 1502
# ttungl@gmail.com

# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.

 

# Example 1:

# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
# Example 2:

# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

# Constraints:

# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # sol 1: sort
        # time O(nlogn) space O(1)
        arr.sort() # O(nlogn)
        diff = abs(arr[1]-arr[0])
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])!=diff:
                return False
        return True
    
        # sol 2:
        # time O(n) space O(1)
        minarr = min(arr)
        gap = (max(arr) - minarr)/(len(arr)-1)
        if gap==0: return True
        i = 0
        while i < len(arr):
        	# compare curr val to the min val plus number of gaps.  
            if arr[i] == minarr + i*gap:  
                i += 1
            else:
                diff = arr[i] - minarr 
                if diff % gap !=0: return False
                # swap to the right index.
                index = int(diff/gap)
                if arr[index] == arr[i]: return False
                arr[index], arr[i] = arr[i], arr[index]
        return True

        
        
        