queue = []
actualPath = []
exploredPath = []

def expand(tree, node):

	if node not in tree:
		exploredPath.append(node)
		return

	list = tree[node]
	list.sort()
	for i in list:
		queue.append(i)

	print("Actual Path: ", actualPath)

	#for i in range(0, len(list)):
		#temp = actualPath[i] + queue[i]
		#actualPath.append(temp)


	exploredPath.append(node)
	
def algo(tree, node, queue, rNode, gNode):	
	queue.append(rNode)
	while len(queue) != 0:
		dequeuedNode = queue.pop(0)
		if dequeuedNode  == gNode:
			print("Goal has found")
			print("Traversed Path: ", exploredPath)
			print("Actual Path: ", actualPath)
			return
		if dequeuedNode not in exploredPath:
			expand(tree, dequeuedNode)	
	print("Goal does not exist")
	
rootNode = 'A'
goalNode = 'F'	
tree = {'A':['B', 'C'], 'B':['D', 'A'], 'C':['E', 'F']}

algo(tree, rootNode, queue, rootNode, goalNode)


