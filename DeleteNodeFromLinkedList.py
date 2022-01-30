from LinkedList import LinkedListHelper
import random
inputFromUser = [4,5,1,9]
linked_list  = LinkedListHelper.createListFromArray(inputFromUser)
LinkedListHelper.printLinkedList(linked_list)


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


randomNumber = random.randint(0,len(inputFromUser)-2)
temp = linked_list
while randomNumber:
    temp = temp.next
    randomNumber  -=  1

NodeToDelete =  temp
print("Node  to Delete  : " ,NodeToDelete.val )
deleteNode(NodeToDelete)
LinkedListHelper.printLinkedList(linked_list)




