h = input("Enter height in m: ")
h = float(h)
w = input("Enter weight in kg: ")
w = float(w)
BMI = w/(h**2)
print(BMI)
if BMI >= 30:
    print("obesity")
elif BMI > 25 and BMI < 29:
    print("overweight")
elif BMI > 18.5 and BMI < 25:
    print("normal")
else:
    print("underweight")