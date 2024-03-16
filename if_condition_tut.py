indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter a dish name: ")

if dish in indian:
    print(f'{dish} is indian')
elif dish in chinese:
    print(f'{dish} is chinese')
elif dish in italian:
    print(f'{dish} is italian')
else:
    print("I don't know")

n = input("Enter a number: ")
n = int(n)
num_type = "Number is even" if n % 2 == 0 else "Number is odd"
print(num_type)