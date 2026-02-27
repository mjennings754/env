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

#Return the alphabet sum for each word in a list.

def alphabet_sum(words):
    res = []
    for word in words:
        total = sum(ord(char.lower()) - 96 for char in word if char.isalpha())
        res.append(total)
    return res

words = ["apple", "dog", "library"]
print(alphabet_sum(words))