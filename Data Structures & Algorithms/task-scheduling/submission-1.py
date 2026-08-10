class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        charArr=[0]*26
        max_repeat=0

        for i in range(0,len(tasks)):
            x=ord(tasks[i])-ord('A')
            charArr[x]+=1
            if max_repeat<charArr[x]:
                max_repeat=charArr[x]

        highest=[]

        for i in range(0,26):
            if charArr[i]== max_repeat:
                highest.append(i)
        x=len(highest)
        y=len(tasks)

        print(x)


        if x<=n+1:
            used=max_repeat*x
            minimum= (max_repeat-1)*(n+1)+(x)
            idle=minimum-used
            rem=y-used
            if rem>idle:
                minimum+=(rem-idle)
        else:
            minimum = max_repeat*(len(highest)-1)
            if minimum < len(tasks):
                return len(tasks)
        return minimum
        




            

        
        