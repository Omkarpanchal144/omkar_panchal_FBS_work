# Set correct credentials
correct_id = "Omkar8999"
correct_pw = "Omkar@123"

# Give user 3 chances
for attempt in range(1, 4):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == correct_id and password == correct_pw:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials! Try again.")
        print("Attempts left:", 3 - attempt)
        print()

# If all 3 attempts are used
else:
    print("3 incorrect attempts! Access Denied.")
