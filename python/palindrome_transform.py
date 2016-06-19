'''
https://community.topcoder.com/tc?module=Static&d1=help&d2=sampleProblems

Example Division Two Problem Statement
(From Single Round Match 96)

A palindrome is a number that is the same whether it is read from left-to-right or right-to-left. For example, 121 and 34543 are both palindromes. It turns out that nearly every integer can be transformed into a palindrome by reversing its digits and adding it to the original number. If that does not create a palindrome, add the reverse of the new number to itself. A palindrome is created by repeating the process of reversing the number and adding it to itself until the number is a palindrome.

Create a class Transform that contains the method palindrome, which takes a number N that is to be transformed and returns a number that is the resultant palindrome from this process. Of course if N is already a palindrome, return it without changing it. Though it is theorized that all numbers can be transformed to palindromes in this way, some numbers do not converge in a reasonable amount of time. For instance, 196 has been carried out to 26,000 digits without finding a palindrome. So if the method finds that the resultant palindrome must be greater than 1,000,000,000, return the special value -1 instead.

DEFINITION
Class: Transform
Method: palindrome
Parameters: int
Returns: int
Method signature (be sure your method is public): int palindrome(int N);

NOTES
- Leading zeroes are never considered part of a number when it is reversed. For instance, 12's reverse will always be 21 regardless of whether it is represented as 12, 012, or 0012. Examples with leading zeroes use the leading zeroes for clarity only.

TopCoder will ensure the validity of the inputs. Inputs are valid if all of the following criteria are met:
- N will be between 1 and 10000 inclusive.

EXAMPLES
Worked examples:
Example 1: N = 28
28 + 82 = 110
110 + 011 = 121, a palindrome. Return 121

Example 2: N = 51
51 + 15 = 66, a palindrome. Return 66

Further examples:
Example 3: N = 11, return 11
Example 4: N = 607, return 4444
Example 5: N = 196, return -1


'''
'''
input output
5
28 121
51 66
11 11
607 4444
196 -1
'''


def palin_Trans(N):
	while (N!=N[::-1]):
		N=str(int(N)+int(N[::-1]))
		if int(N)> 1000000000:
			N=-1
			break
	return N
		
	
for i in xrange(int(input())):			
	print palin_Trans(str(raw_input()))



