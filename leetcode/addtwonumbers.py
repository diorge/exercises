# https://leetcode.com/problems/add-two-numbers/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val and (
            (self.next is None and other.next is None) or (self.next == other.next)
        )

    def __repr__(self):
        return f"({self.val}, {repr(self.next)})"


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    pointer1: Optional[ListNode] = l1
    pointer2: Optional[ListNode] = l2

    result: Optional[ListNode] = None
    current: Optional[ListNode] = None

    carry = 0

    while pointer1 is not None and pointer2 is not None:
        added = pointer1.val + pointer2.val + carry
        carry, digit = divmod(added, 10)
        if current is None:
            result = ListNode(digit)
            current = result
        else:
            current.next = ListNode(digit)
            current = current.next
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    assert result
    assert current

    while pointer1 is not None:
        added = pointer1.val + carry
        carry, digit = divmod(added, 10)
        current.next = ListNode(digit)
        current = current.next
        pointer1 = pointer1.next

    while pointer2 is not None:
        added = pointer2.val + carry
        carry, digit = divmod(added, 10)
        current.next = ListNode(digit)
        current = current.next
        pointer2 = pointer2.next

    if carry > 0:
        current.next = ListNode(carry)

    return result


if __name__ == "__main__":
    lhs = ListNode(2, ListNode(4, ListNode(3)))
    rhs = ListNode(5, ListNode(6, ListNode(4)))
    actual = add_two_numbers(lhs, rhs)
    expected = ListNode(7, ListNode(0, ListNode(8)))
    print(actual, expected)
    assert actual == expected
