import math

accuracy = 0.00001 #the lower this value is the highr is the accuracy but increases response time
total = 0
li = []

def func(x):
    #this try and except is to not crash when we are deviding by zero
    try:
        # define your function here
        # myfunc =(math.sin(x))/x
        myfunc = pow(x,2)
        return  myfunc
    except:
        return 0


def loop(a,b):
    #looping thorugh the values and adding them to a list
    for i in range(int(a/accuracy),int(b/accuracy)):
        li.append(func(i*accuracy))

def sum():
    global total
    #looping through the list to get final result
    for i in li:
        total = total+i
    return total*accuracy
    

def main():
    
    a = float(input("Enter the lower limit: "))
    b = float(input("Enter the upper limit: "))
    loop(a,b)
    print('The integration is:' ,sum())
    


main()