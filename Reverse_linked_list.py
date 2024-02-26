'''Given the head of a singly linked list, reverse the list, and return the reversed list.
Example1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example2:
Input: head = [1,2]
Output: [2,1]

Example3:
Input: head = []
Output: []'''

class Solution(object):
    def reverseList(self, head):
        # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return prev       # Return the prev pointer to get the reverse linked list...
