# https://leetcode.com/problems/add-two-numbers/description/
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional["ListNode"], l2: Optional["ListNode"]) -> Optional["ListNode"]:

        # Use a dummy head so new result nodes can be appended without
        # special-casing the first node.
        dummy = ListNode()
        current = dummy
        carry = 0

        # Continue while either list has digits left, or while a final carry
        # still needs to become its own node.
        while l1 or l2 or carry:
            # Missing nodes count as 0 once one list is shorter than the other.
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the two digits and any carry from the previous column.
            total = val1 + val2 + carry
            carry = total // 10

            # Store only the ones digit in this result node.
            current.next = ListNode(total % 10)
            current = current.next

            # Move each input list forward if it still has nodes left.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # The real result starts after the dummy head.
        return dummy.next
