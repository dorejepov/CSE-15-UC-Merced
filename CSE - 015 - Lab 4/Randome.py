# Define a function that takes in a set, represented as a Python list,
# and returns an equivalent set with all duplicates removed
def simplify(A):
# Provide your code here...
    return list(dict.fromkeys(A))
simpA = simplify(["1","2","5","8","12","5"])

def simplify(B):
    return list(dict.fromkeys(B))
simpB = simplify(["3","5","7","8","11","3"])
print "A = ", simplify(A)
print "B = ", simplify(B)

# Expected:
# A =  [1, 2, 5, 8, 12]
# B =  [3, 5, 7, 8, 11]

print



# Define a function that takes in a set and returns its power set
# The result should be represented as a list of lists, ex: [[], [1], [2], [1, 2]]
def power_set(A):
    # Provide your code here...
    w = len(A)
    for i in range(1 << w):
        print([A[j] for j in range(w) if (i & (1 << j))]

# Testing the power_set function
print "P([1, 2, 3]) =", power_set([1, 2, 3])
print "P([]) =", power_set([])

# Expected:
# P([1, 2, 3]) =  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# P([]) = [[]]
