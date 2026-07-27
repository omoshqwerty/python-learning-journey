name = input("Enter your name: ")
mark1 = int(input("Enter 1st mark: "))
mark2 = int(input("Enter 2nd mark: "))
mark3 = int(input("Enter 3rd mark: "))

average = (mark1+mark2+mark3)/3

if average >= 90:
    grade = "A"
elif average >=75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

status = "Passed" if average >= 50 else "Failed"
print("="*40)
print("     Student Report     ")
print("="*40)
print(f"{name} scored average of {average:.1f} and got grade {grade}")
print(f"Status: {status}")
if "a" in name.lower():
    print("Fun fact: your name has an 'a' in it!")
print("="*40)
