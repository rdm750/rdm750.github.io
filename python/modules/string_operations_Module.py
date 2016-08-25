'''
string operations reverse,anti vowel,remove dpulicates
median of a list,pangram,common substring,
top3 most common in a word,operations to make a palindrome string,


Hackerrank.com,written in CodeAcademy class,

Rohit Malgaonkar

'''
from collections import Counter
from collections import OrderedDict


def reverse(text):
    w=[]
    a=len(text)
    for var in text:
        if a==0:
            break    
        w.append(text[a-1])
        a-=1
    
    for var in w:
        test = ''.join(w)
    
    print test
    return test
#----
def anti_vowel(test):
    
    test1=[]
    for char in test:
        if char != 'a' and char!='e' and char!='i' and char!='o' and char!='u' and char != 'A' and char!='E' and char!='I' and char!='O' and char!='U':
            test1.append(char)    
    return ''.join(test1)
    
#--
#duplicate removal
def remove_duplicates(list_int):
    test_list = list_int 
    list_new=[]
    for num in list_int:
        
        if num not in list_new:
            list_new.append(num)
            
    return list_new
    
#-----
def median(lst):
    lst_new=sorted(lst)
    if len(lst_new)%2==0:
        median1 = len(lst_new)/2
        median2=median1-1
        median=(lst_new[median1]+lst_new[median2])/2.0 
    elif len(lst_new)<1:
        return lst_new[0]
    else:
        median1 = len(lst_new)/2
        median = lst_new[median1]
    return median
#-------

'''Enter your code here. Read input from STDIN. Print output to STDOUT 
checks for alternating characters and prints required deletions
ABABA  no deletions
5
AAAA    3 deletions
BBBBB   4 deletions
ABABABAB 0 deletions
BABABA 0 deletions
AAABBB 4 deletions

'''	
#for i in range(int(input()):
#word=str(raw_input())

def del_Alter_str(test_word):
    word=str(test_word)
    k=0 
    for c in range(len(word)):
    	if c>0:
    		if word[c] == word[c-1]:
    			k+=1
    return k

#----------
def pangram(line):
	count=0
	lista=[]
	test='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for A in line:
	    if A.lower() in test and A.lower() not in lista:
	        count+=1
	        lista.append(A.lower())
	    else:
	        pass#print '#'
	
	if count==26:
	    print 'pangram'
	else:
	    print 'not pangram'

#--------------
def common_substr(stra,strb):
    stra=set(stra)
    strb=set(strb)
    if stra.intersection(strb):
        print 'YES'
    else:
        print 'NO'

#---
'''
from collections import OrderedDic
from collections import Counter
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
'''
def Most_Common(stra):
	a=Counter(stra)
	a=OrderedDict(sorted(a.items(),key= lambda x: (-x[1],x[0])))
	c=0
	for k,v in a.iteritems():
	    if c<3:
	        print k,v
	        c+=1

def PalinOper(word):
    res=0    
    for k in xrange(len(word)/2):
        res+=abs(ord(word[k])-ord(word[-(k+1)]))
    return res

if __name__ ==' __main__':
	reverse(test)
	anti_vowel(test)
	remove_duplicates(list_int)
	median(lst)	
        del_Alter_str(n,test)
	pangram(line)
	common_subtr(stra,strb)
	Most_Common(stra)
        PalinOper(word)

