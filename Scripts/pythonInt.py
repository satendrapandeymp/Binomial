import time
import sys, time
import matplotlib.pyplot as plt


__doc__ = "This is using python capacity to store big integers"

# taking arguments as input
n = int(sys.argv[1])
k = int(sys.argv[2])

# starting time
time1 = time.time()

# Using symmytry
if k< n/2:
    k = n-k

# loop to calculate ncr
rownum = n
newValue=1
for iteration in range (rownum):
    newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )

    if iteration == k:
        break

# printing relevent details
print newValue
print newValue%1026
print time.time() - time1
 
