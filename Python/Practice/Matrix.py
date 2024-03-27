A = []
Row = int(input("Enter the size of Row: "))
Colunm = int(input("Enter the size of Column: "))
for row in range(Row):
    a = []
    for column in range(Colunm):
        a.append(int(input()))
    A.append(a)

print("Matrix A:")
for row in range(Row):
    for column in range(Colunm):
        print(A[row][column], end=" ")
    print()

B = []
Row2 = int(input("Enter the size of Row: "))
Colunm2 = int(input("Enter the size of Column: "))
for row in range(Row2):
    b = []
    for column in range(Colunm2):
        b.append(int(input()))
    B.append(b)

print("Matrix B:")
for row in range(Row2):
    for column in range(Colunm2):
        print(B[row][column], end=" ")
    print()

while True:
    choice = int(input("Click 1.Add \t 2.Subtract \t 3.Multiply \t 0.Exit: "))
    if choice == 1 or choice == 2:
        if Row == Row2 and Colunm == Colunm2:  # Check dimensions for addition/subtraction
            result = [[0 for _ in range(Colunm)] for _ in range(Row)]
            for row in range(Row):
                for column in range(Colunm):
                    if choice == 1:  # Addition
                        result[row][column] = A[row][column] + B[row][column]
                    elif choice == 2:  # Subtraction
                        result[row][column] = A[row][column] - B[row][column]
            print("Result:")
            for r in result:
                print(r)
        else:
            print("Matrix dimensions do not match for addition or subtraction!")
    elif choice == 3:
        if Colunm == Row2:  # Check dimensions for multiplication
            result = [[0 for _ in range(Colunm2)] for _ in range(Row)]
            for row in range(Row):
                for column in range(Colunm2):
                    for k in range(Row2):
                        result[row][column] += A[row][k] * B[k][column]
            print("Result:")
            for r in result:
                print(r)
        else:
            print("Matrix dimensions do not match for multiplication!")
    elif choice == 0:
        print("Exiting...")
        break
    else:
        print("Invalid input! Please try again.")
