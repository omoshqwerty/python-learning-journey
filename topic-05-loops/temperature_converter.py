temp = float(input("Enter temperature in °C: "))
fah = (temp*9/5)+32
print(f"Temperature in Fahrenhite: {fah:.1f}F")
if temp <= 0:
    print("Freezing")
elif temp <= 15:
    print("Cold")
elif temp <= 25:
    print("Mild")
else:
    print("Hot")
