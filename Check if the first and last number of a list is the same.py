import random

B = []
for i in range(1, 5):
    B = B + [random.randrange(0, 6)]

print("The given list is:", B)


def LD(A):
    print(A[0] == A[len(A) - 1])
    return ""


print(LD(B))

