'''
https://code.google.com/codejam/contest/351101/dashboard#s=p2
Input 

Output 
4
hi
yes
foo  bar
hello world

Case #1: 44 444
Case #2: 999337777
Case #3: 333666 6660 022 2777
Case #4: 4433555 555666096667775553

'''

def dial_pad(test):
	dialpad ={}
	dialpad['0']='+'
	dialpad['1']=''
	dialpad['2']='ABC' 
	dialpad['3']='DEF'
	dialpad['4']='GHI'
	dialpad['5']='JKL'
	dialpad['6']='MNO'
	dialpad['7']='PQRS'
	dialpad['8']='TUV'
	dialpad['9']='WXYZ'
	dialpad['*']='*'
	dialpad['1']=''  #nothing on phone  
	dialpad['#']=' '  #space
	
	for s in test:
		for k,v in dialpad.items():
			if s in v.lower():
				print k*(v.lower().index(s)+1),
				
				
	print	
				
for i in xrange(int(input())):
	dial_pad(str(raw_input()))
	
	


