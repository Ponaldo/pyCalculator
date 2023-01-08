

def main():
    print("Here the python calculator , use the * for multiplication and the ** for exponent")
    calceq = str(input("What you trynna calculate: "))
    for i in calceq:
        if i.isalpha():
            print("Do not input any letters into the calculator!")
            x = "true"
            break
    if x != "true":
        print("The answer is: " + str(eval(calceq)))


main()
