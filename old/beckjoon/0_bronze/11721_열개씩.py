stringA = input()

while(len(stringA) > 0):
    print(stringA[:10])
    stringA = stringA.replace(stringA[0:10],'')


