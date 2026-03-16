# n=int(input(" How many numbers you want to add ? "))

# sum=0
# def total ():
#     global sum
#     for i in range(n):
#     number = int(input("Enter a number : "))
#     sum += number

# print(sum)


n = int(input("How many numbers you want to add? "))

total = 0

def add_numbers():
    global total
    for i in range(n):
        number = int(input("Enter a number: "))
        total += number
    print(total)

    
add_numbers()


