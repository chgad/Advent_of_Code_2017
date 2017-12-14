# In this file im testing the runtime of my code "varify_other" against the
# code "varify, seen below, of a friend of mine.
# i do this with the time module and calculating the average of 1000000 times
# due to the fact that the run time is heavily dependet on my pc's processes.


from captcha_solving import varify_other
import time

def calculateRunTime(function, *args):
    startTime = time.time()
    result = function(*args)
    return time.time() - startTime, result

def varify(integer):
    inputStr = str(integer) * 2
    inputLen = int(len(inputStr) / 2)
                
    summation = 0
    for idx in range(0,inputLen):
        if inputStr[idx] == inputStr[idx + int(inputLen / 2)]:
            summation += int(inputStr[idx])
                                                      
    return summation
#c=calculateRunTime(varify_other,1212)
#d=calculateRunTime(varify,1212)

def middle_runtime(N,func,*args):
    summation = 0
    for i in range(N):
        summation += calculateRunTime(func,*args)[0]
    return summation/N

a=middle_runtime(1000000,varify_other,1212)
b=middle_runtime(1000000,varify,1212)

print(a)
print(b)
print(a-b)


