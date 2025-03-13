from typing import List





class Solution:
    def findKthLargest(self, nums1: List[int], k: int) -> int:

        tmp = self.par_sort(nums1)
        print(tmp[len(tmp)-k])
        return 0

    def par_sort(self, nums):
        if len(nums) < 2:
            return nums
        center = len(nums) // 2
        lf = self.par_sort(nums[:center])
        rg = self.par_sort(nums[center:])
        return self.par_son_sort(lf, rg)

    def par_son_sort(self, l, r):
        ll = 0
        rr = 0
        nums_tmp = []
        while ll < len(l) and rr < len(r):
            if l[ll] < r[rr]:
                nums_tmp.append(l[ll])
                ll += 1
            else:
                nums_tmp.append(r[rr])
                rr += 1
        if ll < len(l):
            nums_tmp.extend(l[ll:len(l)])
        if rr < len(r):
            nums_tmp.extend(r[rr:len(r)])
        return nums_tmp


if __name__ == '__main__':
    s = Solution()
    nums2 = [1, 2, 3, 4, 5, 6,5,4,3,2,1, 0]
    s.findKthLargest(nums2, 3)
