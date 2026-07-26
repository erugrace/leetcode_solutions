# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # COACH ANALYSIS:
        # Your logic is almost correct, but there is a bug in how you handle the lists.
        # In the 'if l1 and not l2' and 'if not l1 and l2' blocks, you are missing the 
        # addition of the previous 'carry' to the current node's value.
        # Also, using three separate 'if' statements inside the while loop causes 
        # the pointer to move multiple times in one iteration if both l1 and l2 exist.
        #
        # TIME COMPLEXITY: O(max(N, M)) - Optimal
        # SPACE COMPLEXITY: O(max(N, M)) - Optimal (for the result list)
        #
        # HINT: Use a single 'total = carry' at the start of the loop, then 
        # add l1.val and l2.val conditionally if the nodes exist.
        
        dummy = ListNode(None)
        newHead = dummy
        carry = 0
        while l1 or l2:
            total = carry
            if l1 and l2:
                total = (l1.val + l2.val) + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                total = (l1.val + carry)
                l1 = l1.next
            elif not l1 and l2:
                total = (l2.val + carry)
                l2 = l2.next
            dummy.next = ListNode(total%  10 )
            carry = total // 10
            dummy = dummy.next
            
        if carry:
            dummy.next = ListNode(carry)
        return newHead.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna