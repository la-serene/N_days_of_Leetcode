#include "stdio.h"

bool threeConsecutiveOdds(int* arr, int arrSize) {
    for (int i = 0; i < arrSize - 2; i++) {
        if (arr[i] % 2 == 1) {
            // Even
            if (arr[i + 2] % 2 == 0) {
                i += 2;
                continue;
            }

            // Odd
            if (arr[i + 1] % 2 == 1) return true;
            else i += 1;
        }
    }
    return false;
}