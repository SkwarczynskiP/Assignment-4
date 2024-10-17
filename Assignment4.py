# Question 1
# Give an algorithm to solve this problem without sorting the list. (Use a variation of quickselect or use a heap)
# Determine the time and space complexity in terms of n = len(nums) and in terms of k
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, low, high):
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
            nums[high], nums[i] = nums[i], nums[high]
            return i

        def quickSelect(nums, low, high, k):
            if low == high:
                return nums[low]

            pivot = partition(nums, low, high)

            if pivot == k:
                return nums[pivot]
            elif pivot < k:
                return quickSelect(nums, pivot + 1, high, k)
            else:
                return quickSelect(nums, low, pivot - 1, k)

        return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

# Worst Case Time Complexity (in terms of n): O(n^2)
#     If a the pivot selection is poor, runtime greatly increases.
#     T(n) = n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 = O(n^2)
# Worst Case Time Complexity (in terms of k): O(n^2)
#     If the pivot selection is poor, runtime greatly increases. The same reasoning as above.
# Worst Case Space Complexity (in terms of n): O(n)
#     Space usage is dependent on the depth of recursion stack, which is influenced by array size.
# Worst Case Space Complexity (in terms of k): O(n)
#     Space usage is dependent on the depth of recursion stack, which is influenced by array size.
#     The size of k does not affect the call stack.


# Question 2
# Give an algorithm to solve this problem such that addNum has (amortized) time complexity O(logn) and findMedian has O(1)
# https://leetcode.com/problems/find-median-from-data-stream/description/

class Solution2:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]

# Time Complexity of addNum: O(logn)
#     The method performs several heap push and pop operations, which each are all O(logn).
# Time Complexity of findMedian: O(1)
#     The method simply returns either the median value or the opposite of the max heap's root.
#     There are no loops, only a few simple operations.