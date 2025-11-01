from typing import List, Optional

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove_set = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next:
            if prev.next.val in remove_set:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
