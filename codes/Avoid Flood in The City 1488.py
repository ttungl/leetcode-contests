# Avoid Flood in The City 1488.

# Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

# Given an integer array rains where:

# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:

# ans.length == rains.length
# ans[i] == -1 if rains[i] > 0.
# ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

# Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

 

# Example 1:

# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.
# Example 2:

# Input: rains = [1,2,0,0,2,1]
# Output: [-1,-1,2,1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day, we dry lake 2. Full lakes are [1]
# After the fourth day, we dry lake 1. There is no full lakes.
# After the fifth day, full lakes are [2].
# After the sixth day, full lakes are [1,2].
# It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
# Example 3:

# Input: rains = [1,2,0,1,2]
# Output: []
# Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
# After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
# Example 4:

# Input: rains = [69,0,0,0,69]
# Output: [-1,69,1,1,-1]
# Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
# Example 5:

# Input: rains = [10,20,20]
# Output: []
# Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
 

# Constraints:

# 1 <= rains.length <= 10^5
# 0 <= rains[i] <= 10^9


# reference: https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697703/python-greedy-with-a-heap

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
    	# sol 1:
    	# + First populate all rainy days on each lake.
    	# + For each day, 
    	# 	+ if a rainy day of a lake is filled, return empty list.
    	# 	+ if a lake is rained during a day, 
    	# 	we get the next day the lake is going to be rained in the future,
    	# 	then we put this next day to the closest day (min-heap)
    	# 	so we pop it from the min-heap to a dry day to fill up the lake
    	# 	that will be rained on closest day in the future.  
    	
    	# time O(n) space O(n)

    	closest = [] # store the next rainy days 
    	d = collections.defaultdict(collections.deque)
    	
    	# populate the rainy days of lakes
    	for i, lake in enumerate(rains):
    		d[lake].append(i)
    	
    	res = []
    	
    	for day, lake in enumerate(rains):
    		# this rainy day's lake is filled.
    		if closest and closest[0]==day:
    			return []
    		
    		if not lake: # rains[i]==0 # dry
    			if not closest:  # get closest that's already seen.
    				res.append(1) 
    			else: # remove closest day when a lake is flooded.
    				closest_day = heapq.heappop(closest)
    				res.append(rains[closest_day]) # dry this lake
    		
    		else:  # no dry (aka. rain)
    			raindays = d[lake]
    			raindays.popleft() # already checked.
    			if raindays:
    				closest_day = raindays[0] # closest day of next rainy days
    				heapq.heappush(closest, closest_day)
    			res.append(-1) 
    	return res 


























































