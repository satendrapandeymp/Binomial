import sys, time
import matplotlib.pyplot as plt


__doc__ = "Using pascal tree method"


time1 = time.time()

n = int(sys.argv[1])
k = int(sys.argv[2])

def triangle(rows):
    time1 = time.time()
    time_arr = []
    num_arr = []
    for rownum in range (rows+1):

        if (rownum%100 == 0):
            time_arr.append(time.time() - time1)
            num_arr.append(rownum)
            print "Done with : ", rownum

        newValue=1
        PrintingList = list()
        for iteration in range (rownum):
            newValue = newValue * ( rownum-iteration ) * 1 / ( iteration + 1 )
            PrintingList.append(int(newValue))
    return PrintingList, time_arr, num_arr 

# Driver Program to test ht above functionresukl
result, time_arr, num_arr = triangle(n)

print result[k-1] % 1026



plt.plot(num_arr, time_arr, 'bo', num_arr, time_arr, 'k')
plt.title('Time analysys of ncr')
plt.ylabel('Time Taken in seconds')
plt.xlabel('value of N')
plt.grid(True)
plt.show()
