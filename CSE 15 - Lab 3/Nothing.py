from logic import TruthTable

keepgoing = 'Y'
props = []

while keepgoing == 'Y':
    prop1 = raw_input()
    props.append(prop1)
    keepgoing = raw_input("Would you like to enter more [Y/N]: ")

myTable = TruthTable(props)

print 'Your Program uses propositonal variables,' myTable.vars

#print '----------'
#print myTable.table
#print
in = myTable.vars
props2 =[]

i = 0
while i < len(in):
    props2.append(raw_input("Enter meaning of " + inside[i] + ': '))
    i+= 1

value = []
for i in myTable.table:
    value.append(i[1])
for r in value:
     if (r[2] == 1):
          print 'Your description is consistent when:'
          print 'It is not the case when', props2[0]
          print 'It is not the case when', props2[1]
          break
     else:
        print 'Your description is inconsistent'
        print 'It is not the case when', props2[0]
        print 'It is not the case when', props2[1]
        break
