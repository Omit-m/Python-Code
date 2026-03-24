# my_list = [10, 20, 30, 40, 50]


# print(my_list[-1]) # 50 (last element)
# print(my_list[-2]) # 40 (Second last element)




def palindrome_fun(word):

    if word == word[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")


palindrome_fun(input("input a word : "))


