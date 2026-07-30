class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        largest=0
        n=len(s)

        for i in range(n):
            start=i
            temp=k+1
            un_matched=-1

            while temp!=0 and i < n-1:
                i+=1
                if s[i] != s[start]:
                    temp-=1
                    if un_matched ==-1:
                        un_matched=i
            # print(i,start, temp)
            # print(start,i)
            if temp !=0:
                start=max(start-temp+1,0)
                largest=max(largest,i-start+1)
            else:
                largest=max(largest,i-start)
            i=un_matched
        return largest
