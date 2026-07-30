class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        start=0
        end=m-1

        row = 0

        while start<=end:
            mid = (start + end)//2
            x= matrix[mid][0]
            if target == x:
                return True
            if target < x:
                if mid == 0:
                    return False
                y=matrix[mid-1][0]
                if y < target < x:
                    row=mid-1
                    break
                end =mid-1
                
            else:
                if mid == end:
                    row = end
                    break
                y=matrix[mid+1][0]
                if x < target < y:
                    row = mid
                    break
                start = mid+1
            
        start=0
        end=n-1

        while start <= end:
            mid = (start+end)//2
            
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                end=mid-1
            else:
                start=mid+1

        return False

            