from logic import TruthTable

proposition1 = raw_input("Enter Proposition 1:\n")

proposition2 = raw_input("Enter Proposition 2:\n")

myTable1 = TruthTable(['p','q'],[proposition1])

myTable2 = TruthTable(['p','q'],[proposition2])

print myTable1.table

print myTable2.table

if myTable1.table == myTable2.table:
 print 'The Proposition are equivalent.'

else:
    print 'The Proposition are not equivalent.'
