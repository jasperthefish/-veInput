# recursively input numbers till the number is negative

n = float(input("Enter a number: "))

# def recursive(num):
#     if num < 0:
#         print("The number is negative.")
#         return
#     if num > 0:
#         print("The number is positive.")
#     return 


def negative(num):
    if num < 0:
        return
    num = float(input("Enter a number: "))
    negative(num)

negative(n)