class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num == 1) return true;
        long lo = 1;
        long hi = num;

        while(lo < hi){
            long mid = lo + (hi - lo)/2;
            long res = mid * mid;
            if(res == num) return true;
            else if(res < num) lo = mid + 1;
            else hi = mid;
        }

        return false;
    }
};