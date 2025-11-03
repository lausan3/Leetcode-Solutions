# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Brute force approach:
        # initialize an empty list
        # for each triplet of nodes, find all local minima and maxima
        #   append these to the list
        # return min and max
        #
        # Time: O(n), Space: O(n)

        mini_and_maxi = []

        if not head.next:
            return [-1, -1]

        prev, curr, nex = head, head.next, head.next.next
        i = 1

        while nex:
            prev_v, curr_v, nex_v = prev.val, curr.val, nex.val

            # local minima or maxima
            if (
                prev_v > curr_v < nex_v or
                prev_v < curr_v > nex_v
            ):
                mini_and_maxi.append(i)

            prev = curr
            curr = nex
            nex = nex.next
            i += 1

        if len(mini_and_maxi) < 2:
            return [-1, -1]

        print(mini_and_maxi)

        min_distance = 100_000
        for i in range(1, len(mini_and_maxi)):
            min_distance = min(min_distance, mini_and_maxi[i] - mini_and_maxi[i - 1])

        max_distance = mini_and_maxi[-1] - mini_and_maxi[0]

        return [min_distance, max_distance]