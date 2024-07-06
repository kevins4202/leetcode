#include "../stdc++.h"
using namespace std;

class MyQueue {
public:
    stack<int> a, b;
    MyQueue() {
        
    }
    
    void push(int x) {
        while(!a.empty()){
            b.push(a.top());
            a.pop();
        }

        a.push(x);

        while(!b.empty()){
            a.push(b.top());
            b.pop();
        }
        
    }
    
    int pop() {
        int x = a.top();
        a.pop();
        return x;
    }
    
    int peek() {
        return a.top();
    }
    
    bool empty() {
        return a.empty();
    }
};
