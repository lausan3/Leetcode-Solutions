class MyQueue {
public:
    MyQueue() {}
    
    void push(int x) {
        inStk.push(x);
    }
    
    // removes the element from in front of queue and returns that element
    int pop() { 
        // we need to reverse the input sequence for getting result acc to queue
        if(outStk.size() > 0){
            int outPop = outStk.top();
            outStk.pop();
            return outPop;
        } else {
            while (!inStk.empty()) {
                int reverseInt = inStk.top();
                inStk.pop();
                outStk.push(reverseInt);
            }
            
            int outPop = outStk.top();
            outStk.pop();
            return outPop;
        }
    }
    
    // get the front element
    int peek() {
        // we need to reverse the input sequence to get result acc to queue
        // we need to reverse the input sequence for getting result acc to queue
        if(outStk.size() > 0){
            return outStk.top();
        } else {
            while (!inStk.empty()) {
                int reverseInt = inStk.top();
                inStk.pop();
                outStk.push(reverseInt);
            }
            
            return outStk.top();
        }
    }
    
    // returns whether the queue is empty
    bool empty() {
        return (inStk.size() == 0 && outStk.size() == 0) ;
    }

private:
    stack<int> inStk;
    stack<int> outStk;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */