# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

class TrackNumber(object):
  def __init__(self, numbers = ''):
    self.numbers = numbers

  def parse(self, numbers):
    nums = numbers.upper()
    r = re.compile('(?P<first>[A-Z]+)?(?P<number>\d+)(?P<last>[A-Z]+)?')
    answ = [m.groupdict() for m in r.finditer(nums)]
    return answ