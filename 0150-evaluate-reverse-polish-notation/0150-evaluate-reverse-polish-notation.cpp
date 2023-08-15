class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;

        for (int i = 0; i < tokens.size(); i++) {
            string token = tokens[i];

            // if token is a number, push to stack
            if (token.size() > 1 || isdigit(token[0])) {
                stk.push(stoi(token));
            // else, find out what operator it is and perform it it
            } else {
                if (token == "+") {
                    int num1 = stk.top();
                    stk.pop();
                    int num2 = stk.top();
                    stk.pop();
                    stk.push(num1 + num2);
                } else if (token == "-") {
                    int num1 = stk.top();
                    stk.pop();
                    int num2 = stk.top();
                    stk.pop();
                    stk.push(num2 - num1);
                } else if (token == "*") {
                    int num1 = stk.top();
                    stk.pop();
                    int num2 = stk.top();
                    stk.pop();
                    stk.push(num1 * num2);
                } else {
                    int num1 = stk.top();
                    stk.pop();
                    int num2 = stk.top();
                    stk.pop();
                    stk.push(num2 / num1);
                }
            }
        }

        return stk.top();
    }
};