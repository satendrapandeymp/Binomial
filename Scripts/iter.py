import sys, time
import matplotlib.pyplot as plt


__doc__ = "In this i'm not using python inbuilt data structure to store integer but simply storing that in long int and using dynamic array to contain results."


# taking arguments as input
n = int(sys.argv[1])
k = int(sys.argv[2])


# compacting the arr
def comp_arr(temp_arr):
    if len(temp_arr) < 350:
        return temp_arr

    arr = temp_arr[-350:]
    arr.sort(reverse = True)
    for i in range(-300,0):
        for j in range(i+1, 0):
            if arr[i]*arr[j] < 9223372036854775807:
                arr[j] = arr[i]*arr[j]
                arr[i] = -1 
                break

    for i in range(200):
        try:
            arr.remove(-1)
            arr.remove(1)
        except:
            try:
                arr.remove(-1)
            except:    
                break
    return  temp_arr[:-350] + arr


# Function for gcd
def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 


# to calculate ncr
def nck(n, k):

    # to store time for analysys
    time1 = time.time()
    time_arr = []
    num_arr = []

    # to use symmytry
    if k< n/2:
        k = n-k

    # declearing variables
    num, den = 1, 1
    res_arr = []
    flag = -1

    # Solving through Iterations
    for i in range(k+1,n+1):
        
        if (i%1000 == 0):
            res_arr = comp_arr(res_arr)
            time_arr.append(time.time() - time1)
            num_arr.append(i)
            print "Done with 1000 more steps, ", i

        num *=  i
        den *=  (i-k)

        # waiting till we reach the maximun integer which can be stored in python
        if num > (9223372036854775807)/(i+1):

            # removing common factors from both side
            hcf = gcd(num, den)
            num = num // hcf
            den = den // hcf
            
            # if still bigger that the given number, Then In append it to arr
            if num > (9223372036854775807)/(i+1):
                res_arr.append(num)
                num = 1
                flag += 1

        if den > (9223372036854775807)/(i+1-k) and 1 == 1:
            for m in range(-1 * len(res_arr), 0):
                hcf = gcd(res_arr[m], den)
                res_arr[m] = res_arr[m] // hcf
                den = den // hcf 
                if den < 1000000:
                    break         

            if den > (9223372036854775807)/(i+1-k):
                print "Shaka laka boom boom"      

    res_arr.append(num)
    return den, res_arr, time_arr, num_arr


def getRes(res_arr, den):
    # As we know that every binomial is a perfect integer
    # so if we decouple these then we may get an integer
    temp = 1
    for num in res_arr:
        hcf = gcd(num, den)
        num = num // hcf
        den = den // hcf
        temp *= (num  % 1026)
        temp =  (temp % 1026)

    # Printing the results
    return temp % 1026

# calling the function
den, res_arr, time_arr, num_arr = nck(n, k)
print getRes(res_arr, den)
#den, res_arr, time_arr1, num_arr1 = nck(n, n/2)




#plt.plot(num_arr, time_arr, 'bo', num_arr, time_arr, 'k', num_arr1, time_arr1, 'ro', num_arr1, time_arr1, 'y' )
plt.plot(num_arr, time_arr, 'bo', num_arr, time_arr, 'k')
plt.title('Time analysys of ncr')
plt.ylabel('Time Taken in seconds')
plt.xlabel('value of N')
plt.grid(True)
plt.show()
