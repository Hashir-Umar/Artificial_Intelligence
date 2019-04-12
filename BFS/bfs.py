def expand(tree, node):
	if node not in tree:
		exploredPath.append(node)
		return
	for x in tree[node]:
		queue.append(x)
	queue.sort()
	exploredPath.append(node)
	
def algo(tree, node, queue, rNode, gNode):	
	queue.append(rNode)
	while len(queue) != 0:
		dequeuedNode = queue.pop(0)
		if dequeuedNode  == gNode:
			print("Goal has found")
			print("Actual Path: ", exploredPath)
			return
		if dequeuedNode not in exploredPath:
			expand(tree, dequeuedNode)	
	print("Goal does not exist")
	
rootNode = 'A'
goalNode = 'F'	
tree = {'A':{'B', 'C'}, 'B':{'D', 'A'}, 'C':{'E', 'F'}}
queue = []
exploredPath = []
algo(tree, rootNode, queue, rootNode, goalNode)


