#https://code.google.com/codejam/contest/90101/dashboard#s=p0
import re

test=\
'''
paste input first 5 lines dictionary of words

3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

expected output
Case #1: 2
Case #2: 1
Case #3: 3
Case #4: 0

'''

print test

L,D,N= map(int,raw_input().split())

di=''
for i in xrange(D):
	di+=str(raw_input())+'\n'
for k in xrange(N):
	test= str(raw_input()).replace("(","[").replace(")","]")
	#print re.findall(test,di),'*'*5  # outputs results['abc', 'bca'] *****
	print 'Case #1: ' + str(len(re.findall(test,di)))
	


