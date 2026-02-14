list1 = [1, 2, 3, "hello", "testing", 49.0]
newlist = [item for item in list1 if isinstance(item, (int))]

print(newlist)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
number_5 = nested[1][1]
print(number_5)

# check if a number in palindrome

def is_palindrome(n):
    original = str(n)
    reversed = original[::-1]

    if original == reversed:
        print("True")
    else:
        print("False")

is_palindrome(989)