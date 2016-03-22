# -*- coding: utf-8 -*-
#!/usr/bin/env python

import unittest

from track import TrackNumber

class TrackNumberParseTest(unittest.TestCase):

  def setUp(self):
    self.tn = TrackNumber()

  def testSingleTrack(self):
    answer = self.tn.parse('RJ255255138CN')
    self.assertEqual(1, len(answer))

  def testMultiplicityTrack(self):
    answer = self.tn.parse('RJ255255138CN, RS431632444NL, 11945295679')
    self.assertEqual(3, len(answer))

  def testEmptyTrackParse(self):
    answer = self.tn.parse('')
    self.assertEqual(0, len(answer))

  def testSingleTrackParse(self):
    answer = self.tn.parse('RJ255255138CN')
    self.assertEqual(answer[0].number, '255255138')
    self.assertEqual(answer[0].first, 'RJ')
    self.assertEqual(answer[0].last, 'CN')

  def testSingleOnlyNumberTrackParse(self):
    answer = self.tn.parse('11945295679')
    self.assertEqual(answer[0].number, '11945295679')
    self.assertFalse(answer[0].first)
    self.assertFalse(answer[0].last)

class TrackNumberValidTest(unittest.TestCase):

  def setUp(self):
    self.tn = TrackNumber()

  def validWraper(self, num, ans):
    answer = self.tn.parse(num)
    valid = self.tn.valid(answer[0])
    if ans:
      self.assertTrue(valid)
    else:
      self.assertFalse(valid)

  def testValidOfInternationalTrackNumberFalse(self):
    self.validWraper('RJ222222221CN', False)

  def testValidOfInternationalTrackNumberFalse2(self):
    self.validWraper('1194529567922', False)

  def testValidOfInternationalTrackNumberFalse3(self):
    self.validWraper('RK0267053CN', False)

  def testValidOfInternationalTrackNumberTrue(self):
    self.validWraper('RJ482508186CN', True)

  def testValidOfInternationalTrackNumberTrue1(self):
    self.validWraper('RK026705563CN', True)

if __name__ == '__main__':
  unittest.main()