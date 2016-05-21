# -*- coding: utf-8 -*-

'''
uses regex pattern to get data from text file using optional match and capture groups
example  extract 'ABCD07' and '80' from the following line in file

.
.
.
ABCD0      0      1     4     833       0       0       0       5       0        41  -         
ABCD1      0      1     5     860       0       0       0       5       0        43  -         
ABCD2      0      1     8     858       0       0       0       5       0        43  -         
ABCD3      0      1     9     858       0       0       0       5       0        43  -         
.
.
.
extracts ABCD01 41, ABCD1 43  from above lines...
regexpattern:r'(ABCD\d{1,2})(:?\s+\d+){9}(\s+\d{1,2})'     

tested at http://pythex.org/

'''

import os
import re

test1= open("test12","w")
dr1=os.getenv("HOME")+'/Downloads/test'
for (dirname, dirs, files) in os.walk(dr1):
	for fil in files:
		print fil
		fileop=open(dr1+"/"+fil,"r")
		test1.write(fil+'\n')
		for linerd in fileop:
			regexpat=r'(VPPA\d{1,2})(:?\s+\d+){9}(\s+\d{1,2})'
			match = re.findall(regexpat,linerd)
			for mat in match:
				print mat
				test1.write(' '.join(mat)+'\n')
		test1.write('\n')	
		print len(match),'***********************'
		fileop.close()
test1.close()
