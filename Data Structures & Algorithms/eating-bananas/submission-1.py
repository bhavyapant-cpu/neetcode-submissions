class Solution:
    def calc_hrs(self, mid, arr):
        hrs=0
        for i in range (0,len(arr)):
            hrs+=((arr[i]//mid) + (1 if arr[i]%mid else 0))
        # print(mid,hrs)
        return hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start=1
        end=max(piles)

        while start <= end:
            mid = (start+end)//2
            hrs=self.calc_hrs(mid,piles)
            if h<hrs:
                 start=mid+1
            else:
                end=mid-1  
        return start if max(piles)>start else max(piles)
        