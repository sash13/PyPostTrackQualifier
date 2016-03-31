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
      'url': 'http://www.wedoexpress.com/',
      'len': [13, 13],
      'mask': ['WD*********CN', 'WD#********CN']  
    },
    # UPS
    {
      'name': 'UPS',
      'url': 'http://www.ups.com',
      'len': [18, 9, 10, 12],
      'mask': ['1Z!!!!!!!!!*******', '*********', '**********', '************']  
    },
    {
      'name': 'GATI',
      'url': 'http://www.gati.com/',
      'len':  [12],
      'mask': ['GAT*********']
    },
    {
      'name': 'XRU',
      'url': 'http://www.xru.com',
      'len':  [14, 13, 12],
      'mask': ['XRU***********', 'XRU**********', 'XRU*********']
    },
    {
      'name': 'EWE',
      'url': 'https://www.everfast.com.au',
      'len':  [13, 10],
      'mask': ['##*********##', '**********']
    },
    {
      'name': 'Ouya',
      'url': 'http://www.ouyawuliu.com',
      'len':  [12],
      'mask': ['************']
    },
    {
      'name': 'EX',
      'url': 'http://www.007ex.com',
      'len':  [13],
      'mask': ['##*********##']
    },
    {
      'name': 'BlueSky',
      'url': 'http://www.blueskyexpress.com.au',
      'len':  [],
      'mask': []
    },
    {
      'name': 'Eyou',
      'url': 'http://www.eyoupost.com/',
      'len':  [],
      'mask': []
    },
    {
      'name': 'coe',
      'url': 'http://www.coe.com.hk/',
      'len':  [10, 14],
      'mask': ['**********', '**************']
    },
    {
      'name': 'UPU',
      'url': 'http://www.upu.com',
      'len':  [13],
      'mask': ['##*********##']
    },
    {
      'name': 'TNT',
      'url': 'http://www.tnt.com',
      'len':  [13, 13, 9, 6],
      'mask': ['GD*********WW', 'GE*********WW', '*********', '******']
    },
    {
      'name': 'IMX',
      'url': 'http://www.imxlogis.com/',
      'len':  [16, 12],
      'mask': ['****************', '************']
    },
    {
      'name': 'shpostwish',
      'url': 'http://www.shpostwish.com',
      'len':  [11],
      'mask': ['***********']
    },
    {
      'name': 'ruston',
      'url': 'http://www.ruston.cc',
      'len':  [11],
      'mask': ['***********']
    },
    {
      'name': 'DTDC',
      'url': 'http://dtdc.com/',
      'len':  [14, 11],
      'mask': ['**************', '***********']
    },
    {
      'name': 'Aramex',
      'url': 'http://www.aramex.com/',
      'len':  [20, 12, 11, 10],
      'mask': ['********************', '************', '***********', '**********']
    },
    {
      'name': 'OneWorld',
      'url': 'http://www.oneworldexpress.com/',
      'len':  [13, 8, 12],
      'mask': ['##*********GB', 'CZL*****', '************']
    },
    {
      'name': 'Bpost',
      'url': 'http://www.bpost.be/',
      'len':  [],
      'mask': []
    },
    {
      'name': 'DPEX',
      'url': 'http://www.dpex.com/',
      'len':  [11],
      'mask': ['DP*********']
    },
    {
      'name': 'DPDuk',
      'url': 'http://www.dpd.co.uk',
      'len':  [15, 14, 10],
      'mask': ['**************!', '**************', '**********']
    },
    {
      'name': 'Asiax',
      'url': 'http://www.asiax.jp/',
      'len':  [11],
      'mask': ['AX*********']
    },
    {
      'name': 'fexp',
      'url': 'http://www.4fexp.com/',
      'len':  [12, 16, 14],
      'mask': ['************', '****************', '**************']
    },
    {
      'name': 'Flywayex',
      'url': 'http://www.flywayex.com/',
      'len':  [12, 14],
      'mask': ['##*********!', '**************']
    },
    {
      'name': 'Midline',
      'url': 'http://www.midlinebd.com/',
      'len':  [16, 12],
      'mask': ['****************', '************']
    },
    {
      'name': 'Directlink',
      'url': 'http://www.directlinktrackedplus.com',
      'len':  [11],
      'mask': ['DT*********']
    },
    {
      'name': 'fedex',
      'url': 'http://www.fedex.com',
      'len':  [15, 12, 10],
      'mask': ['***************', '************', '**********']
    },
    {
      'name': 'TOLL',
      'url': 'http://www.tollgroup.com',
      'len':  [12, 9],
      'mask': ['************', '*********']
    },
    {
      'name': 'UBX',
      'url': 'http://www.ubxpress.com/',
      'len':  [15,14,11],
      'mask': ['UBX************', 'UBX***********', '***********']
    },
    {
      'name': 'GLS',
      'url': 'http://gls-group.eu/',
      'len':  [13, 20, 14, 12, 11, 10],
      'mask': ['##*********GB', '********************', '**************', '************', '***********', '**********']
    },
    {
      'name': 'Valueway',
      'url': 'http://www.valueway.ca',
      'len':  [11, 10],
      'mask': ['***********', '**********']
    },
    {
      'name': 'DHL',
      'url': 'http://www.dhl.com',
      'len':  [10, 9],
      'mask': ['**********', '*********']
    },
    {
      'name': 'CANPAR',
      'url': 'http://www.canpar.com/',
      'len':  [12, 11, 10],
      'mask': ['************', '***********', '**********']
    },
    {
      'name': 'Ontrac',
      'url': 'http://www.ontrac.com/',
      'len':  [11],
      'mask': ['##*********']
    },
    {
      'name': 'Nice',
      'url': 'http://www.niceexpress.net/',
      'len':  [16, 14],
      'mask': ['****************', '**************']
    },
    {
      'name': 'px',
      'url': 'http://www.4px.com',
      'len':  [11],
      'mask': ['##*********']
    },
    {
      'name': 'MXE',
      'url': 'http://www.mxe56.com',
      'len':  [16],
      'mask': ['##************##']
    },
    {
      'name': 'Hhexp',
      'url': 'http://www.hh-exp.com/',
      'len':  [11, 13],
      'mask': ['##******###', 'HH***********']
    },
    {
      'name': 'Kuaida',
      'url': 'http://www.kuaidaexp.com',
      'len':  [14, 14],
      'mask': ['##************', '**************']
    },
    {
      'name': 'YANWEN',
      'url': 'http://www.yw56.com.cn/',
      'len':  [13, 13, 13, 11],
      'mask': ['##*********YP', '##*********YW', 'Y#*********CN', 'Y#*********']
    },
    {
      'name': 'DPD',
      'url': 'http://www.dpd.com',
      'len':  [15, 14, 10],
      'mask': ['**************!', '**************', '**********']
    },
    {
      'name': 'CNE',
      'url': 'http://www.cnexps.com',
      'len':  [13],
      'mask': ['*************']
    },
    {
      'name': 'GNL',
      'url': 'http://www.gnl.hk/',
      'len':  [13, 11],
      'mask': ['##*********##', 'GN*********']
    },
    {
      'name': 'ywhyhy',
      'url': 'http://www.ywhyhy.com',
      'len':  [12],
      'mask': ['YWH*********']
    },
    # Default carier if unknow number
    # Must be last element in list
    {
      'name': 'Default',
      'len': [],
      'mask': []  
    }
  ]