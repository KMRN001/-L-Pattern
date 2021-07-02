for row in range(7):
    for col in range(5):
        if (row !=6) and (col == 0):
            print("*", end=" ")
        elif (row == 6):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()