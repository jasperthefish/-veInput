# recursively input numbers till the number is negative

num = int(input("Enter a non-zero number: "))

def recursive(num):
    if num < 0:
        print("The number is negative.")
        return
    if num > 0:
        print("The number is positive.")
    return 