


class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        else if (x == 0) return true;
        else if (x % 10 == 0) return false;
        long y = 0;
        int z = x;

        while (z != 0)
        {
            y = y * 10 + (z % 10);
            z /= 10;
        }

        return x == y;
    }
};