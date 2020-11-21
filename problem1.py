# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

A = [10, 15, 3, 7]
B = A
k = 17



def solution(A):
    A.sort()
    B.sort(reverse=True)
    for x in A:
        for y in B:
            if x + y == k:
                print("Match", x,y)
                raise SystemExit()
            else:
                print("No match", x, y)



solution(A)