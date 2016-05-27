'''
hackerrank Python List Comprehensions passed all test cases
This will generate 3D cordinates x+y+z not equal to N'
******
enter 3D cordinates
1
2
3
enter N This will generate 3D cordinates x+y+z not equal to N
2
******
Rohit Malgaonkar

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
print "enter 3D cordinates"
list_cor = [int(input()) for i in range(3) ]
print 'enter N This will generate 3D cordinates x+y+z not equal to N'
N = int(input())

gen_list = [[x,y,z] for x in range(list_cor[0]+1) for y in range(list_cor[1]+1) for z in range(list_cor[2]+1) if x+y+z != N]
    
print gen_list    
    
