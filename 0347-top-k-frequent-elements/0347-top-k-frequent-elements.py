class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        heap = []
        heapq.heapify(heap)
        result = []

        for num, count in count.items():
            heapq.heappush(heap, (-count, num))

        for i in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result