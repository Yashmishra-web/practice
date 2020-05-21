try:
    inp=int(input("Enter a number: "))
except:
    print("Error wrong value entered:")
    quit()
print(inp, end=' ')
while inp > 1:
    if inp % 2 == 0:
        inp=inp//2
        print(inp,end=' ')
    else:
        inp=inp*3+1
        print(inp, end=' ')