'''
string operations reverse,anti vowel,remove dpulicates
median of a list,pangram,

Hackerrank.com
written in CodeAcademy class
Rohit Malgaonkar
'''

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

if __name__ ==' __main__':
	reverse(test)
	anti_vowel(test)
	remove_duplicates(list_int)
	median(lst)	
        del_Alter_str(n,test)
	pangram(line)

