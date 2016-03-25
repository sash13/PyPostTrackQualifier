# -*- coding: utf-8 -*-

carriers = 
  [
    {
      'name':   'International',
      'regx':   r'([RLVCEU][A-Z])(\d{8})(\d)(\w{2})', #AABBBBBBBBCDD
      'chunk':  [ #AA
                  [
                    {
                      'name': 'Type of parcel',
                      'types':  [
                                  {
                                    'regx': r'R[A-Z]',
                                    'type': 'Registered'
                                  },
                                  {
                                    'regx': r'L[A-Z]',
                                    'type': 'Not Registered'
                                  },
                                  {
                                    'regx': r'V[A-Z]',
                                    'type': 'Letter with declared value'
                                  },
                                  {
                                    'regx': r'C[A-Z]',
                                    'type': 'International parcel'
                                  },
                                  {
                                    'regx': r'E[A-Z]',
                                    'type': 'EMS'
                                  },
                                  {
                                    'regx': r'U[A-Z]',
                                    'type': 'Untracked parcel but required to pass customs procedures'
                                  }
                                ]
                    }
                  ],
                  #BBBBBBBBC
                  [
                    {
                      'name':   'Number',
                      'chunk':  [
                                  {
                                    'regx': r'(\d{8})\d',
                                    'type': 'Parcel number'
                                  },
                                  {
                                    'regx': r'\d{8}(\d)',
                                    'type': 'Checksum of number'
                                  },
                                ]
                    }
                  ],
                  #DD
                  [
                    {
                      'name': 'Country of origin',
                      'type':  'iso3166'
                    }
                  ]
                ]
    }
  ]