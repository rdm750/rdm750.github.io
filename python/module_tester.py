import palindrome
import unique_substrings
import string_operations_Module
import int_operations_Module

palindrome.palindromes(100,2000),'\n'
print unique_substrings.uniq_substring('ababaacabbc'),'\n'
print string_operations_Module.reverse('rohit'),'\n'
print string_operations_Module.anti_vowel('rohit'),'\n'
print [x for x in range(100)][2:50:4],'\n'
print string_operations_Module.median([x for x in range(100)][2:50:4]),'\n'
print string_operations_Module.remove_duplicates([3,11,22,1,22,2,3,33,4,77]),'\n'
print int_operations_Module.max([3,11,22,1,22,2,3,33,4,77])
print int_operations_Module.remov_dupl([3,11,22,1,22,2,3,33,4,77])
print string_operations_Module.del_Alter_str('AAABBB')
for i in xrange(25):
	print int_operations_Module.fibonacci(i),',',
print '\n'
for i in xrange(1,11):
        print int_operations_Module.fib(i,0,1),',',
int_operations_Module.pascal(10)

test=sorted([3,11,22,1,22,2,3,33,4,77])
test2=[5,8,1,3,7,9,2]
t=len(test)
print 'binary search get index of 22 in array ',test,'of length ',t
print int_operations_Module.search(test,22,0,t)
int_operations_Module.partition(test2)
print '\n',int_operations_Module.pairs(test2,2)

