class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while(n!=1 and n not in seen):
            seen.add(n)
            new_num = 0
            while(n>0):
                
                new_num+=(n%10)**2
                n = n//10
           
            n = new_num
        return n==1