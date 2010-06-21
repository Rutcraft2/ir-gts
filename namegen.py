#!/usr/bin/python

from array import array
from binascii import hexlify

namelist = {
    0x01: '',
    0x21: '0',
    0x22: '1',
    0x23: '2',
    0x24: '3',
    0x25: '4',
    0x26: '5',
    0x27: '6',
    0x28: '7',
    0x29: '8',
    0x2a: '9',
    0x2b: 'A',
    0x2c: 'B',
    0x2d: 'C',
    0x2e: 'D',
    0x2f: 'E',
    0x30: 'F',
    0x31: 'G',
    0x32: 'H',
    0x33: 'I',
    0x34: 'J',
    0x35: 'K',
    0x36: 'L',
    0x37: 'M',
    0x38: 'N',
    0x39: 'O',
    0x3a: 'P',
    0x3b: 'Q',
    0x3c: 'R',
    0x3d: 'S',
    0x3e: 'T',
    0x3f: 'U',
    0x40: 'V',
    0x41: 'W',
    0x42: 'X',
    0x43: 'Y',
    0x44: 'Z',
    0x45: 'a',
    0x46: 'b',
    0x47: 'c',
    0x48: 'd',
    0x49: 'e',
    0x4a: 'f',
    0x4b: 'g',
    0x4c: 'h',
    0x4d: 'i',
    0x4e: 'j',
    0x4f: 'k',
    0x50: 'l',
    0x51: 'm',
    0x52: 'n',
    0x53: 'o',
    0x54: 'p',
    0x55: 'q',
    0x56: 'r',
    0x57: 's',
    0x58: 't',
    0x59: 'u',
    0x5a: 'v',
    0x5b: 'w',
    0x5c: 'x',
    0x5d: 'y',
    0x5e: 'z',
    0xab: '!',
    0xac: '?',
    0xad: '(CMA)',
    0xae: '.',
    0xaf: '...',
    0xb0: '(BLT)',
    0xb1: '(SLSH)',
    0xb2: '`',
    0xb3: "'",
    0xb4: '(QT)',
    0xb5: '(QT)',
    0xb9: '(',
    0xba: ')',
    0xbb: '(M)',
    0xbc: '(F)',
    0xbd: '+',
    0xbe: '-',
    0xbf: '(AST)',
    0xc0: '#',
    0xc1: '(EQL)',
    0xc3: '~',
    0xc4: '(CLN)',
    0xc5: '(SEMI)',
    0xc6: '(CLB)',
    0xc7: '(CLB)',
    0xc8: '(HRT)',
    0xc9: '(DMD)',
    0xca: '(STR)',
    0xcb: '0',
    0xcc: 'O',
    0xcd: '(SQR)',
    0xce: '(TRI)',
    0xcf: '(DMD)',
    0xd0: '@',
    0xd1: '(NOTE)',
    0xd2: '%',
    0xd3: '(SUN)',
    0xd4: '(WTF)',
    0xd5: '(UMBR)',
    0xd6: '8',
    0xd7: '^_^',
    0xd8: '^_^',
    0xd9: '>.<',
    0xda: '-.-',
    0xdb: '(UP)',
    0xdc: '(DWN)',
    0xdd: 'ZZ',
    0xff: ''
}

def namegen(namebytes):
    arr = array('B')
    arr.fromstring(namebytes)
    name = ''
    for i in range(len(arr)):
        try:
            name += namelist.get(arr[i])
        except Exception:
            print 'error generating name: character 0x%x unhandled' % arr[i]
            exit(1)
    return name
