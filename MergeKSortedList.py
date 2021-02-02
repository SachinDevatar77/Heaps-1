# Time Complexity: O(nk logk) - Total nk number of elements going inside a priority queue and k at elements particular time
# Space complexity: O(K)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        minHeap = []
        
        # iterate through lists and check if list[i] not equal to Null if not add that into heap
        for i in range(len(lists)):
            if lists[i] != None:
                
                #adding value, index and next value
                heapq.heappush(minHeap, (lists[i].val , i , lists[i].next))
        
        #create a dummy for the reference of next node
        dummy = ListNode(0)
        curr = dummy
        # check till len(minHeap) != 0 and pop form minHeap 
        while len(minHeap) != 0:
            value, index, node = heapq.heappop(minHeap)
            
            if node != None:
                heapq.heappush(minHeap, (node.val, index, node.next))
            
            # attach new node in incresing order and continue by curr
            curr.next = ListNode(value)
            curr = curr.next
         
        # return dummy.next which has my increasing order list
        return dummy.next
