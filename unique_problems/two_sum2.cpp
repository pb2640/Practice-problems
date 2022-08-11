class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int low = 0;
        int high = numbers.size()-1;
        while(low<high){
            int tsum = numbers[low]+numbers[high];
            if(tsum==target){
                return {low+1,high+1};
            }
            else if(target>tsum){
                low++;
            }
            else{
                high--;
            }
        }
        return {-1,-1};
    }
};