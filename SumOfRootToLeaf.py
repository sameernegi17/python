import binarytree

def find_numbers(root,result,output):

    result.append(str(root.value))

    if not root.left and not root.right:
        output.append(int("".join(result),2))
        return

    if root.left:
        find_numbers(root.left,result,output)
        result.pop(-1)

    if root.right:
        find_numbers(root.right,result,output)
        result.pop(-1)



def sumRootToLeaf(root):

    output = []
    find_numbers(root,[],output)
    return sum(output)

arr = [1,0,1,0,1,0,1]

root = binarytree.build(arr)

print(root)
print("Result : ",sumRootToLeaf(root))




