class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)> len(nums2):
            nums1,nums2=nums2,nums1
        
        l=0
        r=len(nums1)
        half=(len(nums1)+len(nums2)+1)//2
        while True:
            mid = (l+r)//2
            Aleft=nums1[mid-1] if mid >0 else float("-inf")
            Aright=nums1[mid] if mid < len(nums1) else float("inf")
            Bright= nums2[half - mid] if half-mid < len(nums2) else float("inf")
            Bleft= nums2[half - mid -1] if half-mid >0 else float("-inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(nums1)+len(nums2))%2 == 1:
                    return float(max(Aleft,Bleft))
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2.0


            if Aleft > Bright:
                r=mid-1
            else:
                l=mid+1
        return -1.0

        