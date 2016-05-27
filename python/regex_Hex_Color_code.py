'''
detects hex color codes
for example in CSS style sheets

enter number of lines and paste line by line to test
avoides selectors #BED and #Cab
'''
print "\
11 \n\
#BED \n\
{\n\
    color: #FfFdF8; background-color:#aef;\n\
    font-size: 123px;\n\
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);\n\
}\n\
#Cab\n\
{\n\
    background-color: #ABC;\n\
    border: 2px dashed #fff;\n\
}   \n\
"


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    strline = str(raw_input())
    pattern = r'(?:(.)?)(#[0-9A-f]{3,6})(?:[;,.)]{1})'
    match = re.findall(pattern,strline)
    for tup in match:
        print tup[1]
