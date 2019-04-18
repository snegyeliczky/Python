def fibonacci2(n):
    fibonacciList = []
    for i in range(n):
        if i==0:
            fibonacciList.append(0)
        elif i==1 or i==2:
            fibonacciList.append(1)
        else: 
            fibonacciList.append(fibonacciList[i-1]+fibonacciList[i-2])
        print(str(i+1)+" : "+str(fibonacciList[i])) 


fibonacci2(int(input("add meg ")))

    

