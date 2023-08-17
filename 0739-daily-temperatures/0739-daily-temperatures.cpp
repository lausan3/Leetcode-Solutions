class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();

        // make a stack of pairs <temperature, day index>
        stack<pair<int, int>> stk;

        vector<int> answer(n, 0);

        for (int i = n - 1; i >= 0; i--) {
            int currTemp = temperatures[i];

            // starting from the last item, check if the temperature at the top of the stack is 
            // greater than the current temp, if so, subtract the indicies and put it in that day's slot in the 
            // return vector, if not, pop the top of the stack, we won't need it anymore
            while (!stk.empty() && stk.top().first <= currTemp) {
                stk.pop();
            }
            
            if (!stk.empty() && stk.top().first > currTemp) {
                answer[i] = stk.top().second - i;
            }

            stk.push(pair<int, int>(currTemp, i));
        }

        return answer;
    }



































    /*
        int n = temperatures.size();
        
        // pair: [index, temp]
        stack<pair<int, int>> stk;
        // create vector with n numbers of 0s
        vector<int> result(n, 0);
        
        // for each temperature, 
        for (int i = 0; i < n; i++) {
            int currDay = i;
            int currTemp = temperatures[i];
            
            // while stack is not empty and the last temperature is less than the current temperature
            while (!stk.empty() && stk.top().second < currTemp) {
                int prevDay = stk.top().first;
                int prevTemp = stk.top().second;
                stk.pop();
                
                result[prevDay] = currDay - prevDay;
            }
            
            stk.push({currDay, currTemp});
        }
        
        return result;
    */
};