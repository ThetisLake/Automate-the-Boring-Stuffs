#! python3

# TODO: Receive input - n matrix

def architect(n):

    totalRange = (n*n)

    #(5,4) < (5,3)
    #(4,5)<(5,5)
    #IF I==j
    #if j==I
    
    for i in range(totalRange):
        print(i+1)
    

architect(4)

'''
1,2,3,4,5
16,17,18,19,6
15,24,25,20,7
14,23,22,21,8
13,12,11,10,9
'''

# at 3,3 it is final
# at 2,3 it is 18
# at 5,2 it is 12

'''
1,2,3,4
12,13,14,5
11,16,15,6
10,9,8,7
'''

'''
1,2,3
8,9,4
7,6,5
'''

