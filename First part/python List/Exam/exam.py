
"""
"""
def palindrome_fun(word):

    if word == word[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


palindrome_fun(input("Input a word : "))