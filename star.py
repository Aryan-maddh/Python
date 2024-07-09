
"""
        
      1
    2   2
  3   3   3
4   4   4   4
        """

# x = int(input("Enter The number of row:- "))
# for a in range(1,x+1):
#     print()
#     for b in range(1,(x+1)-a):
#         print(" ",end=" ")
#     for c in range(0,a):
#         print(f"{a}  ",end=" ")

'''

      * 
    * * *
  * * * * *
* * * * * * *

'''


# n = 5
# for i in range(1,n):
#     print()
#     for k in range(1,n-i):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")

'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

# n = 5
# for i in range(1,n+1):
#     print()
#     for k in range(1,(n+1)-i):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")
# # n = 5
# for i in range(n,0,-1):
#     print()
#     for k in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(1,i*2):
#         print("*",end=" ")

n=5
for i in range(1,n+1):
    print()
    if(i==1 or i==n):
        for i in range(0,n+1):
         print("* ",end="")
    else:

        print("* ",end="")