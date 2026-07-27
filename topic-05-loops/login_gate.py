correct_password = "python123"
password = input("Enter password: ")

if password == correct_password:
    print("Access Granted")
else:
    print("Access Denied")

is_long = len(password) >= 6
print(f"Password longer than 6 characters: {is_long}")

