class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;

        // solution: for every value in nums, get the product of all the values before it (prefix) 
        // and storing them in the position in the output array that it's before, and then multiply them
        // by the postfix product.

        // Prefix Solving
        int prefix = 1;

        for (int i = 0; i < nums.size(); i++) {
            answer.push_back(prefix);

            prefix *= nums[i];
        }

        // Postfix solving - same thing as prefix but in reverse
        int postfix = 1;

        for (int i = nums.size() - 1; i >= 0; i--) {
            answer[i] *= postfix;
            
            postfix *= nums[i];
        }

        return answer;
    }
};