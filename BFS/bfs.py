queue = []
actualPath = []
exploredPath = []

def expand(tree, node):
	
	#Do not expand leaf node 
	if node not in tree:
		exploredPath.append(node)
		actualPath.pop(0)
		return

	chainNode = actualPath.pop(0)
	chainNodeChild = tree[node]
	chainNodeChild.sort()
	
	for child in chainNodeChild:
		queue.append(child)
		actualPath.append(chainNode+child)
	
	exploredPath.append(node)
	
def algo(tree, node, queue, rNode, gNode):	
	queue.append(rNode)
	actualPath.append(rNode)
	while len(queue) != 0:
		dequeuedNode = queue.pop(0)
		if dequeuedNode  == gNode:
			print("Goal has found")
			print("Traversed Path: ", exploredPath)
			print("Actual Path: ", actualPath[0])
			return
		if dequeuedNode not in exploredPath:
			expand(tree, dequeuedNode)
		else:
			actualPath.pop(0)
	print("Goal does not exist")
		
inputFile = open("test.txt","r")
fileText = inputFile.read().splitlines()
inputFile.close()

rootNode = fileText[0][0]
goalNode = fileText[0][2]

tree = {}
fileText.pop(0)
for i in fileText:
	temp = i.split(':')
	tree[temp[0]] = temp[1].split(',')

print("Root Node: ", rootNode)
print("Goal Node: ", goalNode)
print("Tree: ", tree)

algo(tree, rootNode, queue, rootNode, goalNode)


