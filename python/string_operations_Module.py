'''
string operations reverse,anti vowel,remove dpulicates
median of a list,

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

if __name__ ==' __main__':
	reverse(test)
	anti_vowel(test)
	remove_duplicates(list_int)
	median(lst)	

