#A linked list is a data structure featuring nodes, which point to one other node. The first node is considered the head node, and the last one is the tail. Given the head node, you can traverse to any other node in the list
#Standard bare-bones python implementation of singly linked list
class LinkedList:
    def __init__(self,head = None) -> None:
        self.head = head
class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = next
