# https://leetcode.com/problems/median-of-two-sorted-arrays


def median(xs: List[int]) -> float:
    n = len(xs)
    q, r = divmod(n, 2)
    if r == 1:
        return xs[q]
    else:
        return (xs[q - 1] + xs[q]) / 2


def bin_search_index(needle: int, haystack: List[int]) -> int:
    cmin = 0
    cmax = len(haystack) - 1

    while cmax - cmin > 1:
        idx = (cmin + cmax) // 2
        if haystack[idx] < needle:
            cmin = idx
        else:
            cmax = idx

    if haystack[cmin] >= needle:
        return cmin
    elif haystack[cmin] < needle <= haystack[cmax]:
        return cmax
    else:
        return cmax + 1


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        while True:
            # edge cases
            if len(nums1) == 0:
                return median(nums2)
            if len(nums2) == 0:
                return median(nums1)

            # base cases
            # <= 3 is required, can use a bit higher for perf like insertion sort
            if len(nums1) <= 6:
                for n in nums1:
                    insert_idx = bin_search_index(n, nums2)
                    nums2.insert(insert_idx, n)
                return median(nums2)
            if len(nums2) <= 6:
                for n in nums2:
                    insert_idx = bin_search_index(n, nums1)
                    nums1.insert(insert_idx, n)
                return median(nums1)

            median1 = median(nums1)
            median2 = median(nums2)
            if median1 > median2:
                bigger = nums1
                bigger_median = median1
                smaller = nums2
                smaller_median = median2
            else:
                bigger = nums2
                bigger_median = median2
                smaller = nums1
                smaller_median = median1

            removable_count = (min(len(nums1), len(nums2)) - 2) // 2
            new_smaller = smaller[removable_count:]
            new_bigger = bigger[:-removable_count]

            return self.findMedianSortedArrays(new_smaller, new_bigger)
