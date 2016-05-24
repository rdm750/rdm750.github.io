def dial_pad(num):	
	dialpad ={}
        dialpad['0']=''
	dialpad['1']='ABC' 
	dialpad['2']='DEF'
	dialpad['3']='GHI'
	dialpad['4']='JKL'
	dialpad['5']='MNO'
	dialpad['6']='PQRS'
	dialpad['7']='TUV'
	dialpad['8']='WXYZ'
	dialpad['*']='*'
	dialpad['9']=''  #nothing on phone  
	dialpad['#']=' '  #space
	  
	#for key, value in dialpad.iteritems():		
	for char in str(num):
		test = dialpad[str(char)]
		if len(test)!=0:
			print test[0],
	print '\n'

dial_pad('789#66#63234')
dial_pad('22#22')
dial_pad('180024582266')
