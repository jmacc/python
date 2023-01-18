#While Exceptionw

while True:
    try:
        x = int(input("Please enter a number: "))
        print("Perfect")
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")