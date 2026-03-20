def findMedianSortedArrays( nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        median=0
        if(length%2==0):
                index1=length/2
                median=(nums1[int(index1)]+nums1[int(index1)-1])/2
        else:
                median=nums1[int(length/2)]
        return median

      
print(findMedianSortedArrays(   nums1 = [1,2], nums2 = [3,4]))
