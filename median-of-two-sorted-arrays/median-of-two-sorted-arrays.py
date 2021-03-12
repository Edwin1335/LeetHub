class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        new_array = []
        a = 0 if len(nums1) > 0 else None
        b = 0 if len(nums2) > 0 else None

        if a is None and b is None:
            return None

        while a != None or b != None:
            if a != None and a >= len(nums1):
                a = None
            if b != None and b >= len(nums2):
                b = None
            if a is not None and  b is None:
                new_array.append(nums1[a])
                a += 1
            elif b is not None and a is None:
                new_array.append(nums2[b])
                b += 1
            elif a is not None and b is not None:
                if nums1[a] <= nums2[b]:
                    new_array.append(nums1[a])
                    a += 1
                else:
                    new_array.append(nums2[b])
                    b += 1
        
        if len(new_array) % 2 ==0:
            median1, median2 = len(new_array) // 2, (len(new_array) // 2) - 1
        else:
            median1, median2 = len(new_array) // 2, len(new_array) // 2
        
        return (new_array[median1] + new_array[median2]) / 2