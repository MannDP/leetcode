#include <limits.h>

class Solution {
public:
    int reverse(int x) {
        int result = 0;
        while(x) {
            int digit = x % 10;

            // check for overflow
            if (digit >= 0 && result > (INT_MAX - digit)/10) return 0;
            if (digit < 0 && result < (INT_MIN - digit)/10) return 0;
            
            result = result * 10 + digit;
            x = x / 10;
        }

        return result;
    }
};