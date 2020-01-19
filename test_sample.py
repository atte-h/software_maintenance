#######################################
# Atte Hemminki 
# atte.hemminki@student.lut.fi
# LUT University, CT70A3000 Software Maintenance
#######################################

import pytest
from Fibo import Fibo

def test_length():
  # Tests that output is as long as given as an input
  length=10
  startnumber=10
  list = Fibo.fib(length,startnumber)
  l = len(list)
  assert( l == 10 )

def test_startingNumber():
  # Tests first item in the list is not smaller than given as an input
  length=10
  startnumber=4
  list = Fibo.fib(length,startnumber)
  minimi = list[0]
  assert( minimi > startnumber )

def test_charinput():
  # Tests that giving char as input dont make an error
  length="r"
  startnumber=4
  list = Fibo.fib(length,startnumber)
  assert (list != Empty )


