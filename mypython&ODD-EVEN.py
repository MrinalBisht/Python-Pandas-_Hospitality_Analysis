n = input("Enter a number: ")
n = int(n)

if n % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')

#OR

n = input("Enter a number: ")
n = int(n)
num = "Number is even" if n % 2 ==0 else ("Number is odd")
print(num)