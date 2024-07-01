#include "../stdc++.h"
using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        if(a.size() < b.size()){
            string tmp = a;
            a = b;
            b = tmp;
        }
        cout<<"A "<<a<<endl<<"B "<<b<<endl;

        int carry = 0;
        // string ans =

        for(int i = 0; i < b.size(); i++){
            int j = a.size() - 1 - i;
            int k = b.size() - 1 - i;
            
            int curr = (a[j] - '0') + (b[k] - '0') + carry;
            
            carry = curr >= 2 ? 1 : 0;

            a[j] = '0' + curr % 2;
        }

        cout<<a<<endl;

        int index = a.size() - b.size() - 1;

        while(index >= 0 && carry){
            int curr = (a[index] - '0') + carry;
            
            carry = curr >= 2 ? 1 : 0;

            a[index] = '0' + curr % 2;
            // a[index] = '0';
            index--;
        }

        if(carry) {
            a = "1" + a;
        }

        return a;
    }
};