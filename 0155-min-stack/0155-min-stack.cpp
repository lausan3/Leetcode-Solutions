class MinStack {
public:
    MinStack() {};
    
    void push(int val) {
        // push value to normal stack
        stk.push(val);
        
        // if minimum stack is empty or the value is less than the top of the stack, push val to the min stack
        if (minStk.empty() || val < minStk.top().first) {
            minStk.push({val, 1});
        // else if the value is the same as the top of the stack, increase the frequency of the top of the stack by one
        } else if (val == minStk.top().first) {
            minStk.top().second++;
        }
    }
    
    void pop() {
        // if the top of the stack is the same as the top of the minstack, decrement the minstack by one
        if (stk.top() == minStk.top().first) {
            minStk.top().second--;

            // also, if the top of the minstack's counter is 0, then remove it from the minstack
            if (minStk.top().second == 0) {
                minStk.pop();
            }
        }
        stk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minStk.top().first;
    }
private:
    stack<int> stk;
    stack<pair<int, int>> minStk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */