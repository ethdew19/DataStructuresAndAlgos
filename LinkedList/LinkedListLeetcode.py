from Implementation import LinkedList, Node

#Leetcode #206. Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/

#Standard solution
#Time Complexity: O(n), single pass through of linked list
#Space Complexity: O(1), creates a few pointers, that's it in terms of space used
#Notes: remember that this question is just pointer manipulation. Remember that you want your first node pointing to nothing, that gives you the first line of code.The next pointer is obvious once you realize you need to loop through the list while changing it
def reverseLinkedList(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

#Leetcode #141. Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/

#Solution utilizing python dictionary/hashmap
#Time Complexity: O(n), loops through linked list single time. Checking if the head is in the dictionary is a constant time operation
#Space Complexity: O(n), Stores every node in the dictionary if there isn't a cycle
#Notes: This solution doesn't involve any fancy manipulation of the linked list, all you need to do is loop through it. Realize that the nodes themselves are hashable, and each have individual memory addresses. 
def hasCycle(head):
    myDict = {}
    while head:
        if head in myDict:
            return True
        else:
            myDict[head] = 1
        head = head.next
    return False

#Leetcode #21. Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/

#In place iterative solution
#Time Complexity: O(n), where n is the length of both lists combined. Goes through both of the lists
#Space Complexity: O(1) , this algorithm is constant time, with the only space being taken up is the dummy node. The O(n) space for the two lists is already "used" since it is given to the function, so it is ignored.
#Notes: Usage of a dummy node is extremely helpful in these types of problems, and essentially allows you to create your own linked list. Once all of the elements in one list have been added to the list, it is trivial to add the rest of the other list. 
def mergeTwoLists(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    head = dummy = Node(0)
    while l1 and l2:
        if l1.val > l2.val:
            dummy.next = l2
            l2 = l2.next
        else:
            dummy.next = l1
            l1 = l1.next
        dummy = dummy.next
    if l1 or l2:
        dummy.next = l1 or l2
    return head.next


