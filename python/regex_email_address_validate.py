'''

A valid email address follows the rules below: 
- Email must have three basic components: username @ website name . extension. 
- The username can contain: alphanumeric characters, -,. and _. 
- The username must start with an English alphabet character. 
- The website name contains only English alphabet characters. 
- The extension contains only English alphabet characters, and its length can be 1, 2, or 3.

Input Format

name <example@email.com>

The first line contains an integer . 
The next  lines contains a name and an email address separated by a space.

passed all test cases on hackerrank for validating & parsing email addresses. here's my solution

https://www.hackerrank.com/rdm750
Rohit Malgaonkar
run:  python scriptname.py

enter input for number of emails: 1  <enter>
enter emails: 
name <example@email.com> <enter>

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

print 'enter input for number of emails:'
for i in range(int(input())):
    print 'enter emails:'	
    email=str(raw_input())
    emailpat = r'[A-z]+\s[\<\'][A-z][A-z0-9_.-]+@[a-z]+\.[a-z]{1,3}[\>\']'
    match = re.findall(emailpat,email)
    if len(match)!=0:
        print '\n***********************\n'
	print match[0]
    else:
	print 'Invalid'                                                              
                                                               
    
    
   
