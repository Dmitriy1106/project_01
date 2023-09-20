fib1, fib2 = 1,1
i=input("Номер: ")
i=int(i)-2
while i > 0:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
    i-=1
    print("Значение", fib2)