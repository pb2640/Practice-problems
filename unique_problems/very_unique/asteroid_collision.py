class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for new in asteroids:
            while ans and new<0<ans[-1]:
                #collision
                if(abs(new) > ans[-1]):
                    ans.pop()
                    continue
                elif(abs(new)==ans[-1]):
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans