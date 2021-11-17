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

#Leetcode # 19. Remove Nth node from end of list
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

#Two pointer approach
#Time Complexity: O(n), goes through list essentially twice 
#Space Complexity: O(1), only space used is the pointers
#Notes: This problem exemplifies why you should almost always add a dummy node for linked list problems. If you don't create one, and try to return head, it will be incorrect for the edge case of an array with one element
#This also showcases a useful pattern where you have two pointers at seperate places in the list. This is not a tortoise and hare algorithm, since they move at the same speed, but just a specific two pointer algo. 
def removeNthFromEnd(head,n):
    slow = fast = dummy = Node(0,next=head)
    for _ in n:
        fast = fast.next  
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

#Leetcode #876. Middle of the linked list
#https://leetcode.com/problems/middle-of-the-linked-list/

#Tortoise and hare solution
#Time Complexity: O(n). where n is amount of nodes in list
#Space Complexity: O(1), space used by the pointers
#Notes, useful pattern to learn, make sure to think it through so you don't get off by one
def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
    

#Leetcode #143. Reorder List
#https://leetcode.com/problems/reorder-list/

#Tortoise and hare algorithm
#Time Complexity: O(n), you iterate through the list a few times, but each step is linear
#Space Complexity: O(1), space is only used to create the pointers used
#Notes: This solution can be broken down into three parts. 1. Divide the list in half using a tortoise and hare approach. 2. Reverse the second list. 3. Combine the two lists
#The combination of the two lists has the prev and head pointer switching locations between the two lists, the name "prev" is misleading and has nothing to do with it's use in this part of the algorithm
def reorderList(head):
    if not head:
        return head
    slow=fast=head
    while fast.next and fast.next.next:
        fast= fast.next.next
        slow = slow.next
    cur = slow.next
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    slow.next = None
    while prev:
        next = head.next
        head.next = prev
        head = prev
        prev = next
    
#Leetcode #23. Merge K Sorted Lists
#https://leetcode.com/problems/merge-k-sorted-lists/

#Divide and conquer iterative Merge solution
#Time Complexity: O(n * log(k)) , where k is amount of lists to sort and n is length of longest list
#Space Complexity: O(n), the array will have n / 2 elements at first, and will only get smaller
#Notes: This used the same code from leetcode #21 as a helper function. The main strategy is divide and conquer, where you keep merging lists until you end up with one list. 
def mergeKlists(lists):
    if not lists:
        return None
    while len(lists) > 1:
        mergedlists = []

        for i in range(0,len(lists),2):
            l1 = lists[i]
            l2 = lists[1+1] if (i + 1) < len(lists) else None
            mergedlists.append(mergelist(l1,l2))
        lists = mergedlists
    return lists[0]

def mergelist(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    tail = dummy = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if not l1 or not l2:
        tail.next = l1 or l2
    return dummy.next



