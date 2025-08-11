num=float(input("Enter the number to check is it even or odd : "))
if (num==int(num)):
    if(num%2==0):
        print(num ," is an even number.")
    else:
        print(num, " is an odd number.")
else:
    strcheck=str(num)
    n=len(strcheck)
    last_digit=strcheck[n-1]
    if (int(last_digit) % 2 == 0):
        print(strcheck + " is an even number.")
    else:
        print(strcheck + " is an odd number.")

