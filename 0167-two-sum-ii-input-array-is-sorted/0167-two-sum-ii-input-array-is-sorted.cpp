class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Solution: because the input is sorted, we can use a two pointer approach to search for the two
        // values that add up to the target.

        std::vector<int> indexes;
        int l = 0;
        int r = numbers.size() - 1;

        while (l< r)
        {
            int sum = numbers[l] + numbers[r];

            // if sum less than target, adjust by one
            if (sum == target) {
                indexes.push_back(l +1);
                indexes.push_back(r+1);
                return indexes;
            } else if (sum <= target) {
                l++;
            } else {
                r--;
            }
        }

        return indexes;
    }
};