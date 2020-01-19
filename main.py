#######################################
# Atte Hemminki 
# atte.hemminki@student.lut.fi
# LUT University, CT70A3000 Software Maintenance
#######################################

from Fibo import Fibo

lengthOfSeries = int(input("Enter length of the series: "))
startingNumber = int(input("Enter starting number: "))

res = Fibo.fib(lengthOfSeries,startingNumber)
print(res)

f = open("resultFile.txt", "a")
i=0
while i<len(res):
  line = str(res[i])
  f.write(str(line))
  f.write("\n")
  i += 1
f.close()
