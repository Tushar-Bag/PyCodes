



def S(B):
    for i in range(0,len(B)):
        for j in range(i+1, len(B)):
            if (int(B[i])+int(B[j]))==target:
               print("Output: ", [i,j])
    return ""

target = int(input("Target number is: "))
B = input("List is: ")
print(S(B))







