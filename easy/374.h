
 int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        // if(guess(1) == 0) return 1;
        long lo = 1;
        long hi = n;

        while(lo <= hi){
            long mid = lo + (hi - lo)/2;
            int ret = guess(mid);
            if(ret == -1) hi = mid-1;
            else if(ret == 1) lo = mid + 1;
            else return mid;
        }

        return -1;
    }
};