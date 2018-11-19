sum = 0
listfib = [ ]

def printlist() :
    for number in range (n) :
        listfib.append(number)



def fiboEvenSum () :
  for i in listfib :
    if i % 2 == 0 :
      sum += i

print fiboEvenSum(10)
