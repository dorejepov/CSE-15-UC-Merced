from logic import TruthTable

def propositiona1 (flag):
    for i in range (4):
          if list[i][1][0] == list[i][1][1]:
           i += 1
          else:
            flag = 1
    if flag == 0:
        print("Both Propositions are not equal")
    else:
        print("Both Propositions are not equal")

def proposition2 (flag):
    print("Proposition 2 invoked")
    for i in range (4):
          if list[i][1][2] == list[i][1][3]:
           i += 1
    else:
            flag = 1
    if flag == 0:
         print("Both Propositions are equal")
    else:
         print("Both Propositions are not equal")

def proposition3(flag):
    print("Proposition 2 invoked")
    for i in range (4):
          if list[i][1][4] == list[i][1][5]:
           i += 1
          else:
               flag = 1
    if flag == 0:
        print("Both propositions are equal")
    else:
        print("Both propositions are not equal")

list = [ [[0,0] , [0,0,0,0,0,0]] , [[0,1]] , [0,1,0,0,1,1]] , [[1,0] , [1,0,0,0,1,1]] , [[1,1] , [1,1,1,1,1,1,]]
print(list[3][5][1])
pro1 = input("Enter proposition 1")
pro2 = input("Enter proposition 2")
i = 0
flag = 0
if pro1 == "p and p" and pro2 == "q and q":
 proposition1(flag)
if pro1 == "p and q" and pro2 == "q and p":
 proposition2(flag)
if pro1 == "p or q" and pro2 == "q or p":
 proposition3(flag)

else:
    print("Please enter correct propositions of the form x and y or x or y")
