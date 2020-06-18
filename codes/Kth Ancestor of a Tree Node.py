# Kth Ancestor of a Tree Node

# You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the 
# parent of node i. The root of the tree is node 0.

# Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there 
# is no such ancestor, return -1.

# The k-th ancestor of a tree node is the k-th node in the path from that node to the root.

# Input:
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

# Output:
# [null,1,0,-1]

# Explanation:
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

# treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
# treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
# treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
 

# Constraints:

# 1 <= k <= n <= 5*10^4
# parent[0] == -1 indicating that 0 is the root node.
# 0 <= parent[i] < n for all 0 < i < n
# 0 <= node < n
# There will be at most 5*10^4 queries.


##############################################
# notes: This is a Binary Lifting Technique. #
##############################################
# reference: https://leetcode.com/problems/kth-ancestor-of-a-tree-node/discuss/686362/Python-Jump-Parent/578768

class TreeAncestor:
	# sol 1: O(nlogn)
    def __init__(self, n: int, parent: List[int]):
        self.parent = [parent]
        # element [j][i] means the 2^(j-th) ancestor of node i-th.
        # ancestor holds 2^k nodes at each step, so max steps 16 is calculated by the term: 2^k <= 5*10^4. simply log2.
        for j in range(1,16): # or use int(math.ceil(math.log(n, 2)))
        	self.parent.append([])
        	for i in range(n):
        		if self.parent[j-1][i] == -1:
        			self.parent[j].append(-1)
        		else:
        			self.parent[j].append(
        								self.parent[j-1][self.parent[j-1][i]]
        								)

    def getKthAncestor(self, node: int, k: int) -> int:
        while k!=0:
        	index = int(math.log(k, 2)) # calculate log2 k.
        	node = self.parent[index][node] # update node
        	if node==-1 or index==math.log(k,2): # when parent==-1 or index==log2 k.
        		return node 
        	k -= 2**index # reduce k by index power of 2.
        return node # when k=0, found k-th ancestor.


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)

####################
# self.parent after init.
# [[-1, 0, 0, 1, 1, 2, 2]
# [-1, -1, -1, 0, 0, 0, 0]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1, -1, -1]]






























