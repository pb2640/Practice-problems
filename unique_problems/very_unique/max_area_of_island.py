class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        marked = set()
        max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j]
                coord = (i,j)
                if(coord in marked or curr==0):
                    continue
                q = []
                q.append(coord)
                temp_sum = 0
                while(q):
                    coord = q.pop(0)
                    if(coord not in marked):
                        temp_sum+=1
                    else:
                        continue
                    marked.add(coord)
                    
                    i,j = coord
                    #add neighbors if they exist and if they are not zero and not visited
                    if(i-1>=0 and grid[i-1][j]==1 and (i-1,j) not in marked):
                        #add top ele
                        q.append((i-1,j))
                    if(i<len(grid)-1 and grid[i+1][j]==1 and (i+1,j) not in marked):
                        q.append((i+1,j))
                    if(j-1>=0 and grid[i][j-1]==1 and (i,j-1) not in marked):
                        q.append((i,j-1))
                    if(j<len(grid[i])-1 and grid[i][j+1]==1 and (i,j+1) not in marked):
                        q.append((i,j+1))
                # print(temp_sum)
                max_sum = max(max_sum,temp_sum)
        return max_sum