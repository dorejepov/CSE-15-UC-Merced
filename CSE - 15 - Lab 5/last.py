def linearSearch(A, value):
# Provide your code here
    found = False
    position = 0
    while position < len(A) and not found:
        if A[position] == value:
            found = True
        position = position + 1
    return found

print "linearSearch([1, 2, 3, 4, 5], 4):", linearSearch([1, 2, 3, 4, 5], 4)
# Expected True
print "linearSearch(range(900), -1):", linearSearch(range(900), -1)
# Expected False

print
