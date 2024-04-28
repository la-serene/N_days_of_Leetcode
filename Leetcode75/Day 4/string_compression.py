# 443. String Compression
# Medium
# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

# NOTE: the first solution is not an algo :) just found by debugging:')
#       let's work out the 2nd

"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array
chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

arr = ["a", "a", "b", "b", "c", "c", "c"]


def compress1(chars):
    c = chars[0]
    chars.pop(0)
    v = 1
    i = 0
    while i <= len(chars):
        if i == len(chars):
            chars.insert(i, c)
            if v != 1:
                v = str(v)
                j = 0
                for j in range(len(v)):
                    chars.insert(i + j + 1, v[j])
            break

        if chars[i] == c:
            chars.pop(i)
            v += 1
            continue

        c_new = chars[i]
        chars.insert(i, c)
        if v != 1:
            v = str(v)
            j = 0
            for j in range(len(v)):
                chars.insert(i + j + 1, v[j])

            i += (j + 1)

        i += 1
        c = c_new
        chars.pop(i)
        v = 1

    return len(chars)


def compress2(chars):
    s = ""
    c = chars[0]
    v = 1
    for i in range(1, len(chars)):
        if chars[i] == c:
            v += 1

            if i != len(chars) - 1:
                continue

        s += c
        if v != 1:
            s += str(v)
        c = chars[i]
        v = 1

    chars = list(s)
    return len(chars)
