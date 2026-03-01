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