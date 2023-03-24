while True:
    try:
        n = int(input())
        if 0 < n < 101:
            print("vai ter duas!")
        else:
            print("vai ter copa!")


    except EOFError:
        break
#Enquanto o numero do input for maior do que 0 vai ter duas copas, e enquanto for 0 vai ter copa
