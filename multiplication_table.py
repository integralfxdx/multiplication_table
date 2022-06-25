rows=int(input("max rows : "))
columns=int(input("max columns : "))

for i in range(1,rows+1):
    for j in range(1,columns+1):
        print("{} * {} = {}".format(i,j,i*j))
    print()