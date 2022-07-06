class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        strat 2: find the first neg element using binary search and count remaining neg using index
        O(mlogn)
        """
        length = len(grid[0])
        count = 0
        for i in range(len(grid)):
            l = 0
            r = length - 1
            row = grid[i]
            while l <= r:

                mid = (l + r) // 2
                # print(mid,row[mid],row[mid-1])
                if mid == 0 and row[mid] < 0:
                    count += length
                    break
                elif row[mid] < 0 and row[mid - 1] >= 0:
                    count += length - mid
                    break
                elif row[mid] < 0:
                    r = mid - 1
                else:
                    l = mid + 1

            # print(i,count)

        return count

        """
        strat 1: iterate over each element in each row, on first neg number break and calc remaining using index
        """
        # length = len(grid[0])
        # count = 0
        # for i in range(len(grid)):
        #     for j in range(length):
        #         if(grid[i][j]<0):
        #             count+=(length-j)
        #             break
        # return count
