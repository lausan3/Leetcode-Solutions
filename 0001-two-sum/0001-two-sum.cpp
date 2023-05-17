class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> the;
        
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < nums.size(); j++) {
                if (!(i == j)) {
                    if (nums[i] + nums[j] == target) {
                        the.push_back(i);
                        the.push_back(j);
                        return the;
                    }
                }
            }
        }
        return nums;
    }
};