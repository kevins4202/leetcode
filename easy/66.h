#include "../stdc++.h"
using namespace std;


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        if(digits[digits.size() - 1] != 9) {
            digits[digits.size() - 1] ++;
            return digits;
        }

        digits[digits.size() - 1] = 0;
        // carry = 1;

        int i = digits.size() - 2;
        while(i >= 0){
            if(digits[i] == 9) {
                digits[i] = 0;
                // carry = 1;
            } else{
                digits[i] ++;
                return digits;
            }
            i--;
        }

        if(i == -1) digits.insert(digits.begin(),1);
        return digits;
    }
};