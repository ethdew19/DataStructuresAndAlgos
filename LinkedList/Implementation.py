#Standard bare-bones python implementation of singly linked list
#
class LinkedList:
    def __init__(self,head = None) -> None:
        self.head = head
class Node:
    def __init__(self,val,next) -> None:
        self.val = val
        self.next = next
