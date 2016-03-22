# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

class TrackNumber(object):
  def __init__(self, numbers = ''):
    self.numbers = numbers

  def parse(self, numbers):
    answ = []
    nums = numbers.upper()

    for num in nums.split(','):
      regex = r'(?P<first>[A-Z]+)?(?P<number>\d+)(?P<last>[A-Z]+)?'
      group = re.match(regex, numbers) 
      if group:
        answ.append(group.groupdict())

    return answ