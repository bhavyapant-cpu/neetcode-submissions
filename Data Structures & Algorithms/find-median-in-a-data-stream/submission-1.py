class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)  
        self.arr.sort() 

    def findMedian(self) -> float:
        n=len(self.arr)
        print(n)
        if n%2==0:
            return float((self.arr[n//2]+self.arr[(n-1)//2])/2)
        else:
            return float(self.arr[n//2])
        
        