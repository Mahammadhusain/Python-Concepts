# import sys
# print("You entered: ",sys.argv[1], sys.argv[2], sys.argv[3])

import sys
  
add = 0.0
  
# Getting the length of command
# line arguments
n = len(sys.argv)
  
for i in range(1, n):
    add += float(sys.argv[i])
  
print ("the sum is :", add)


# Get all path of python environment Paths
# for i in sys.path:
#     print(i)

# Get Currunt Python interpreter version
print(sys.version)