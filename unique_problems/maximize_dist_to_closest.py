
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        849. Maximize Distance to Closest Person
        ====== Failed attempt========
        capture index,closest index on left,closest index on right
        1st sort by index - closest on left and then closest right -index
        '''
        total = len(seats)
        store = [[0 for i in range(3)] for j in range(total)]
        closest_left,closest_right = 0,0
        for i in range(len(seats)):
            if(seats[i]==1):
                closest_left = i
            store[i][0] = i
            store[i][1] = closest_left
        # print(store) 
        for i in range(len(seats)-1,-1,-1):
            if(seats[i]==1):
                closest_right = i
            store[i][2] = closest_right
        # print(store)
        ans = 0
        for i in range(len(store)):
            ans = max(ans,min(store[i][0]-store[i][1],store[i][2]-store[i][0]))
        return ans
        
        