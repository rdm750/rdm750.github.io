'''
Sunny and Johnny together have  dollars they want to spend on ice cream. The parlor offers  flavors, and they want to choose two flavors so that they end up spending the whole amount.

You are given the cost of these flavors. The cost of the  flavor is denoted by . You have to display the indices of the two flavors whose sum is .
https://www.hackerrank.com/challenges/icecream-parlor

'''
for i in xrange(int(input())):
    mn=(int(input()),int(input()))
    arr = map(int,raw_input().split())
    for k in xrange(len(arr)-1):
        if mn[0]-arr[k] in arr[k+1:]:
             print k+1,arr[k+1:].index(mn[0]-arr[k])+k+2
