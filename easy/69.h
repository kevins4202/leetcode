#include "../stdc++.h"
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if(x == 0) return x;
        if(x < 4) return 1;

        int lo = 2;
        int hi = x;

        while(lo < hi - 1){
            long mid = lo + (hi - lo)/2;

            cout<<lo<<" "<<hi<<" "<<mid<<endl;

            if(mid * mid < x) {
                lo = mid;
            } else if(mid * mid > x){
                hi = mid;
            } else return mid;
        }

        return lo;
    }
};