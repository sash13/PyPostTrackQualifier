# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re
from data import carriers

class TrackNumberView(object):
  def __init__(self, d):
    self.__dict__ = d

class TrackNumber(object):
  def __init__(self, numbers = ''):
    self.numbers = numbers

  def check(self, number=''):
    for carrier in carriers:
      regexp = re.compile(carrier['regx'])
      if regexp.search(number) is not None:
        return carrier
    return carriers[-1] # return Default value

  def parse(self, numbers):
    nums = numbers.upper()
    r = re.compile('(?P<first>[A-Z]+)?(?P<number>\d+)(?P<last>[A-Z]+)?')
    return [TrackNumberView(m.groupdict()) for m in r.finditer(nums)]

  def valid(self, num):
    if num.first is None or num.last is None or num.number is None:
      return False   
    if len(num.number) is not 9:
      return False  

    mult = [8, 6, 4, 2, 3, 5, 9, 7] #const for multiply
    prod = sum(map(lambda inn: int(inn[0])*inn[1], zip(num.number[:8], mult)))

    check = 11 - (prod % 11)  # magic test
    check = check if check > 1 and check <= 9 else 0 if check == 10 else 5 if check == 11 else None
    if not check and check < 0 and check > 9:
      return False 
    if check != int(num.number[-1]):
      return False
    return True