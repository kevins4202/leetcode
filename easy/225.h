#include "../stdc++.h"
using namespace std;

class MyStack {
public:
    queue<int> a;
    queue<int> b;
    
    MyStack() {
        
    }
    
    void push(int x) {
        b.push(x);
        while(!a.empty()){
            b.push(a.front());
            a.pop();
        }

        a = b;
        b = queue<int>();
    }
    
    int pop() {
        int tmp = a.front();
        a.pop();
        return tmp;
    }
    
    int top() {
        return a.front();
    }
    
    bool empty() {
        return a.empty();
    }
};
