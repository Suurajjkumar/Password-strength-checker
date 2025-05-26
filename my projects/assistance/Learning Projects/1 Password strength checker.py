#Mini Project 2: Password Strength Checker
# Goal:
#Ask the user to enter a password and check if it’s strong or weak based on a few conditions.
""""✅ Conditions to Check:
A password is strong if it meets all the following:

Length is at least 8 characters

Contains at least one uppercase letter

Contains at least one lowercase letter

Contains at least one number

Contains at least one special character (like @, #, $, !, etc.)

If any of these are missing, show which condition(s) failed.

🧠 Concepts You’ll Use:
input() to take user input

if, elif, else to check conditions

any(), isupper(), isdigit(), in operator

len() to check length

🧪 Example Input/Output:
Case 1:
pgsql
Copy
Edit
Enter password: Hello123!
Password is strong ✅
Case 2:
diff
Copy
Edit
Enter password: hello
Password is weak ❌
Missing:
- At least 1 uppercase letter
- At least 1 number
- At least 1 special character
- Minimum length of 8 characters
🔧 Your Tasks:
Ask the user to enter a password.

Check each condition one by one.

If all conditions are true → print "Password is strong ✅"

Else → print "Password is weak ❌" and show which checks failed. """


password = input(" Enter the password: ")

#conditions
is_long = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in "@#$%&*[]{}()-=+,<>/!|?^" for char in password)

#check if all conditions are true
if is_long and has_upper and has_lower and has_digit and has_special :
    print("✅ password is strong")
else:
    print("❌ password is weak, missing:")

    if not is_long:
        print("Password is too short")
    if not has_upper:
            print("_At least 1 uppercase letter ")
    if not has_lower:
        print("_At least 1 lowercase letter")
    if not has_digit:
        print("_At least 1 number")
    if not has_special:
        print("At least 1 special character")









