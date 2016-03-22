# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest

from track import TrackNumber

class TrackNumberTest(unittest.TestCase):

  def setUp(self):
    self.tn = TrackNumber()

  def testSingleTrack(self):
    answer = self.tn.parse('RJ255255138CN')
    self.assertEqual(1, len(answer))

  def testMultiplicityTrack(self):
    answer = self.tn.parse('RJ255255138CN, RS431632444NL, 11945295679')
    self.assertEqual(3, len(answer))

  def testSingleTrackParse(self):
    answer = self.tn.parse('RJ255255138CN')
    self.assertEqual(answer[0]['number'], '255255138')
    self.assertEqual(answer[0]['first'], 'RJ')
    self.assertEqual(answer[0]['last'], 'CN')

  def testSingleOnlyNumberTrackParse(self):
    answer = self.tn.parse('11945295679')
    self.assertEqual(answer[0]['number'], '11945295679')
    self.assertFalse(answer[0]['first'])
    self.assertFalse(answer[0]['last'])

if __name__ == '__main__':
  unittest.main()