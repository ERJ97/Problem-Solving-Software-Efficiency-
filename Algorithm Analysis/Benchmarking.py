# Example 1 

import time 

def sumOfN2(n):
    start = time.time()
    theSum = 0

    for i in range(1,n+1):
        theSum = theSum + i
    end = time.time()
    return theSum, end-start
for i in range(5):
    print("Sum is %d required %10.7f seconds" %sumOfN2(10000))



# Example 2 

import time 

def sumOfN3(n):
    return (n * (n + 1)) / 2
def benchmark(n): 
    start_time = time.time()
    result = sumOfN3(n)
    elapsed_time = time.time() - start_time
    print(f"Sum is {result} required: {elapsed_time:.10f} seconds")

    