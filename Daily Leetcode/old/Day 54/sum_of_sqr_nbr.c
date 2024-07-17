// 633. Sum of Square Numbers
// Medium
// https://leetcode.com/problems/sum-of-square-numbers/

/* Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
 */

#include "stdio.h"
#include "math.h"

bool judgeSquareSum(int c) {
    int h = (int) sqrt(c);
    for (long i = h; i >= 0; i -= 1) {
        double res = sqrt(c - i * i);
        long l_res = (long) res;
        if (l_res == res) return true;
    }
    return false;
}