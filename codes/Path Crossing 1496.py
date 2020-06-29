# Path Crossing 1496. 


# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving
# one unit north, south, east, or west, respectively. You start at the origin (0, 0) on
# a 2D plane and walk on the path specified by path.

# Return True if the path crosses itself at any point, that is, if at any time you are on
# a location you've previously visited. Return False otherwise.


# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
 

# Constraints:

# 1 <= path.length <= 10^4
# path will only consist of characters in {'N', 'S', 'E', 'W}


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # sol 1
        # time O(n) space O(n)
        d = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0)}
        res = [[0,0]]
        cur = [0,0]
        for i in path:
            cur = [cur[0] + d[i][0], cur[1]+d[i][1]]
            if cur not in res:
                res.append(cur)
            else:
                return True
        return False
        