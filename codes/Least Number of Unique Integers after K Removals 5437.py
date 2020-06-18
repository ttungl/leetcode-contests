# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    	# sol 1
    	# time O(nlogn) space O(n)
        if k == 0:  # return all unique numbers if no removal.
            return len(set(arr))
        
        d_sorted = sorted(collections.Counter(arr).items(), key=lambda x: x[1]) # sort value.
        
        for i,v in enumerate(d_sorted):
            if k==0: break
            
            d_sorted[i] = (v[0], max(0, v[1] - k)) # update count down
            k -= v[1] # update number of removal k
                         
        res = 0 # count the keys that still have count > 0
        for i in d_sorted:
            if i[1]>0: 
                res += 1
        return res

        # sol 2
        # time O(nlogn) space O(n)
        if k==0: return len(set(arr))

        sorted_count = sorted(collections.Counter(arr).items(), key=lambda x: x[1]) # sort value

        removal = 0
        for key,val in sorted_count:
        	if k >= val:
        		k -= val 
        		removal +=1
        	else:
        		break
        return len(sorted_count) - removal








