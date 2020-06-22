# Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree 5443. 


# Given a weighted undirected connected graph with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between nodes fromi and toi. A minimum spanning tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph. An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. A pseudo-critical edge, on the other hand, is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
# Example 2:



# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.
 

# Constraints:

# 2 <= n <= 100
# 1 <= edges.length <= min(200, n * (n - 1) / 2)
# edges[i].length == 3
# 0 <= fromi < toi < n
# 1 <= weighti <= 1000
# All pairs (fromi, toi) are distinct.


# reference: 
# explain: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/discuss/697761/C++-Solution-enumerating-edges-with-explanation
# code: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/discuss/697761/C++-Solution-enumerating-edges-with-explanation/588088

# https://en.wikipedia.org/wiki/Disjoint-set_data_structure
# disjoint-set | merge-find | union-find : 
#   is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.
#   provides operations to add new sets, to merge exisiting sets, and to determine whether the elements are in the same set.
#   it plays a key role in Kruskal's algorithm for finding the minimum spanning tree.
class UnionFind:
	def __init__(self, n):
		self.id = list(range(n)) # number of vertices
		self.size, self.count = [1]*n, n 

	def find(self, p):
		if self.id[p] != p:
			self.id[p] = self.find(self.id[p])
		return self.id[p]

	def union(self, p, q):
		i, j = self.find(p), self.find(q)
		if i==j: return 
		if self.size[i] < self.size[j]:
			self.id[i] = j
			self.size[j] += self.size[i]
		else:
			self.id[j] = i
			self.size[i] += self.size[j]
		self.count-=1


class KruskalAlgo:
	def kruskal(self, i, j, n, sorted_edges): # pre, ban, num
		uf, totalweights = UnionFind(n), 0
		if i >= 0:
			_, (f,t,w) = sorted_edges[i]
			uf.union(f,t) # from, to.
			totalweights += w
			if uf.count==1: return totalweights
		for edge in range(len(sorted_edges)):
			if edge == i or edge == j: continue
			_, (f,t,w) = sorted_edges[edge]
			if uf.find(f) != uf.find(t):
				uf.union(f,t)
				totalweights += w
				if uf.count==1: break
		return totalweights if uf.count==1 else 1000*1001


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    	# To generate critical and pseudo-critical edges on MSTs, for each edge:
    	# if deleting an edge and recalculating the weights on MST, if the weight is increased, then the edge is critical and we put it to the critical list.
    	# if adding an edge and recalculating the MST that doesn't change in weight, then the edge is pseudo-critical and add it to the pseudo-critical list.
    	sorted_edges = sorted(enumerate(edges), key=lambda x: x[1][2])

    	ka = KruskalAlgo()

    	MSTweights = ka.kruskal(-1,-1,n,sorted_edges)
    	
    	ans = [[],[]]
    	for i in range(len(edges)):
    		curr_totweights = ka.kruskal(-1,i, n, sorted_edges)
    		if curr_totweights > MSTweights:
    			ans[0].append(sorted_edges[i][0])

    		else:
    			curr_totweights = ka.kruskal(i,-1, n, sorted_edges)
    			if curr_totweights == MSTweights:
    				ans[1].append(sorted_edges[i][0])
    	return ans





























