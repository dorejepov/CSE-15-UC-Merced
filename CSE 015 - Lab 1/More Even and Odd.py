a = int(raw_input('Enter your first integer: '))
b = int(raw_input('Enter your second integer: '))
c = int(raw_input('Enter your third integer: '))
d = int(raw_input('Enter your fourth integer: '))
e = int(raw_input('Enter your fifth integer: '))
f = int(raw_input('Enter your sixth integer: '))
g = int(raw_input('Enter your seventh integer: '))
h = int(raw_input('Enter your eighth integer: '))
i = int(raw_input('Enter your ninth integer: '))
j = int(raw_input('Enter your tenth integer: '))

if a%2 == 0:
    a = 0
else:
    a = a
if b%2 == 0:
    b = 0
else:
    b = b
if c%2 == 0:
    c = 0
else:
    c = c
if d%2 == 0:
    d = 0
else:
    d = d
if e%2 == 0:
    e = 0
else:
    e = e
if f%2 == 0:
    f = 0
else:
    f = f
if g%2 == 0:
    g = 0
else:
    g = g
if h%2 == 0:
    h = 0
else:
    h = h
if i%2 == 0:
    i = 0
else:
    i = i
if j%2 == 0:
    j = 0
else:
    j = j

value = a, b, c, d, e, f, g, h, i, j
max = max(value)
if max == 0:
    print 'No ODD numbers where entered.'
else:
    print max, 'is the largest ODD integer.'
