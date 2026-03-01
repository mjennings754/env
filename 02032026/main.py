# sort the list
list1 = [2, 6, 543, 23, 5, 8, 7, 5, 534, 867, 876, 675]

#list1.sort()
#print(list1)

def sort(x):
    n = len(x)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if x[i-1] > x[i]:
                flag = True
                x[i-1], x[i] = x[i], x[i-1]

sort(list1)
print(list1)

# check if palindrome

def check_palindrome(str1):
    original = str1
    new = str(str1)
    if original == new:
        print("True")
    else:
        print("False")

check_palindrome("A man a plan a canal Panama")

# create a password strength function

def check_password_strength(password):
    length_ok = False
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    if len(password) >= 8:
        length_ok = True

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True

        elif not char.isalnum():
            has_special = True

    if length_ok and has_uppercase and has_lowercase and has_number and has_special:
        return "Strong"
    elif length_ok and (has_uppercase or has_lowercase) and has_number:
        return "Medium"
    else:
        return "Weak"
    

password1 = "1Pass#"
password2 = "P@assw0Rd001"
password3 = "Password1"

print(f"'{password1}': {check_password_strength(password1)}")
print(f"'{password2}': {check_password_strength(password2)}")
print(f"'{password3}': {check_password_strength(password3)}")