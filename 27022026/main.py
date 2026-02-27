# determine if a string is palindrome
def check_palindrome(x):
    x = str(x)
    org = x
    new = x[::-1]
    if org == new:
        print("True")
    else:
        print("False")

check_palindrome(121)