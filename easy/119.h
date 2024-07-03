#include "../stdc++.h"
using namespace std;

class Solution {

public:
    vector<int> getRow(int r) {
        vector <int> vect(r+1);
        vect[0] = 1;
        long long value;
        for(int i = 1;i<r;i++){
           value = (long long)vect[i-1]*(r-i+1)/i;
             vect[i] =(int)value;
        }
        vect[r] = 1;
        return vect;
    }
};