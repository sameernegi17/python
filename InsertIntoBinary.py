from binarytree import Node

def getNode(data):

    newNode = Node(data)
    newNode.data = data
    newNode.left = None
    newNode.right = None
    return newNode

def LevelOrder(root, data):
    if (root == None):
        root = getNode(data)
        return root

    if (data <= root.data):
        root.left = LevelOrder(root.left, data)
    else:
        root.right = LevelOrder(root.right, data)
    return root


def constructBst(arr, n):
    if (n == 0):
        return None
    root = None

    for i in range(0, n):
        root = LevelOrder(root, arr[i])

    return root
