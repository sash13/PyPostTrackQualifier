# -*- coding: utf-8 -*-

carriers = [
    {
      'name':   'International',
      'len': [13],
      'mask': ['##*********##']  
    },
    # Wedo express "WD116437123CN"
    {
      'name': 'WeDo',
      'len': [13, 13],
      'mask': ['WD*********CN', 'WD#********CN']  
    },
    # UPS
    {
      'name': 'UPS',
      'len': [18, 9, 10, 12],
      'mask': ['1Z!!!!!!!!!*******', '*********', 
               '**********', '************']  
    },
    # Default carier if unknow number
    # Must be last element in list
    {
      'name': 'Default',
      'len': [],
      'mask': []  
    }
  ]