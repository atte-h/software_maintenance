#######################################
# Atte Hemminki 
# atte.hemminki@student.lut.fi
# LUT University, CT70A3000 Software Maintenance
#######################################

class Fibo: 
  def fib (lengthOfSeries,startingNumber):
    list = []
    i1= 0 # First number
    i2= 1 # Second number
    currentStep = 0

    # For first two steps
    if startingNumber < i1:
      list.append(i1)
      list.append(i2)
      currentStep = 2
    elif startingNumber < i2:
      list.append(i2)
      currentStep = 1

    # From 2....n steps
    while currentStep < lengthOfSeries: 
      i3 = i1 + i2
      i1 = i2
      i2 = i3
      if startingNumber < i3:
        list.append(i3)
        currentStep += 1

    return list

