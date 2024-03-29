class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = 0
        while i < len(nums):
            x = nums[i]
            if x != val:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
            i += 1
        return k


if __name__ == "__main__":
    s = Solution()

    assert s.removeElement([3, 2, 2, 3], 3) == 2
    assert s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
