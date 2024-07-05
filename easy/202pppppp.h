class Solution {
public:
    int next(int n){
        int ret = 0;
        while(n){
            int d = n % 10;
            ret += d * d;
            n /= 10;
        }

        return ret;
    }
    bool isHappy(int n) {
        int slow = n;
        int fast = next(n);

        while(fast != 1 && fast != slow){
            fast = next(next(fast));
            slow = next(slow);
        }

        return fast == 1;
    }

    
};