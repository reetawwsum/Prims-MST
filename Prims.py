from collections import defaultdict

g = defaultdict(dict)
X = [] #Vertex processed so far
costMST = 0 #Cost of Minimum Spanning Tree

with open('edges.txt', 'r') as inputFile:
	lines = inputFile.readlines()
	ints = [int(x) for x in lines[0].split(" ")]
	n = ints[0] # of Vertices
	m = ints[1] # of Edges
	for line in lines[1:]:
		ints = [int(x) for x in line.split(" ")]
		g[ints[0]][ints[1]] = ints[2]
		g[ints[1]][ints[0]] = ints[2]

X.append(1) #Vertex chosen at random
myDict = {}

while len(X) != n:
	#Finding the neighbor with minimum distance
	for v in X:
		temp = {g[v][neighbor]: neighbor for neighbor in g[v].keys() if neighbor not in X}
		if temp != {}:
			myDict[min(temp)] = temp[min(temp)]
	#Adding neighbor to visited Vertices
	X.append(myDict[min(myDict)])
	#Adding the cost of the edge
	costMST += min(myDict)
	myDict = {}

print costMST