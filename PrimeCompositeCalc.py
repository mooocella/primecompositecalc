#This code will determine if an inputted number is prime or composite.
num = int(input("Please enter a positive number: "))
#This while loop will continue to ask to reinput a number until it is positive.
while num < 0 :
    num = int(input("The number must be positive. Please enter a positive number: "))
#If the number is 0 or 1, it will say it's neither prime or composite.
if num == 0 or num == 1 :
    print (str(num) + " is neither prime or composite.")
#For all other numbers, it will divide the given number by the range (2 to the number minus 1)
else:
    for divisor in range (2, num-1):
#if the given number is divisible and the quotient is ), the number is composite.
        if num % divisor == 0:
             print (str(num) + " is a composite number")
             break
#break the code so that once it determines the quotient = 0 once, it does not continue
#otherwise any other number is prime
    else:
         print (str(num) + " is a prime number.")
