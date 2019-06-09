# Exercise 1: Convert a string of characters to a list of numbers by taking the ASCII value of the numbers
def chars_to_nums(c):
    if c == False:
        return "Not the correct result"
    else:
        return [ord(i) for i in c ]
print(chars_to_nums("HELLO WORLD"))

# Exercise 2: Convert a list of numbers to a string of characters by converting the ASCII values to characters
def nums_to_chars(n):
    if n == False:
    #if n == 0:
        return "Not the correct result"
    else:
        return [chr(i) for i in n ]
        #return ''.join(chr(x) for x in n)
print(nums_to_chars([40, 37, 44, 44, 47, 0, 55, 47, 50, 44, 36]))

# Exerscise 3: Implement an encode procedure for the Caesar cipher. It should take in the plaintext as a string, the key as an integer, and a modulus as an integer, which corresponds to the size of the alphabet, and produce the appropriate ciphertext. In most cases the modulus will be 95, since there are 95 printable ASCII characters that we can use. The pair (key, mod) makes up the encryption key.
def caesar_encode(plaintext, key, mod):
    output = ''
    for x in plaintext:
           if x.isalpha():
               num = ord(x)
               num = num + key

               if x.isupper():
                   if num > ord('Z'):
                       num -= 26
                   elif num < ord('A'):
                       num += 26
               elif x.islower():
                   if num > ord('z'):
                       num -= 26
                   elif num < ord('a'):
                       num += 26

               output += chr(num)
           else:
               output += x
    return output
print(caesar_encode("HELLO", 3, 95))

# Exercise 4: Implement the decode procedure for the Caesar cipher. It should take in the ciphertext and the encryption key, and produce the plaintext.
def caesar_decode(ciphertext, key, mod):
    return caesar_encode(ciphertext, -key, mod)
print(caesar_decode("KHOOR", 3, 95))

# Exercise 5: Assuming the following string was encoded with the Caesar cipher, using some unknown encryption key, recover the plaintext. Type your answer in the string 'ex_5_plaintext' below, do not include any characters in the string, other than the recovered plaintext:
integer = True
if (integer == True):
    ex_5_ciphertext = "-HIIJSYCMY=IIF"
    print caesar_decode(ex_5_ciphertext, -6, 95)
else:
    ex_5_plaintext = "Not the correct result"
    print "The message is:", ex_5_plaintext
