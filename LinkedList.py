class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListHelper:
    @staticmethod
    def createListFromArray(arr):
        head = None
        if len(arr):
            head = ListNode(arr[0])
            temp = head
            for idx in range(1,len(arr)):
                temp.next = ListNode(arr[idx])
                temp  = temp.next

        return head

    @staticmethod
    def printLinkedList(head):
        temp = head
        output  =  ""
        while temp:
            output += str(temp.val) + "---->"
            temp  = temp.next
        output += "None"
        print(output)

