#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Acesta este un program test de selectare aleatoare a unei
populații de cromozomi folosind metoda ruletei.
"""

import crmz
import pcrmz
import random


rez = [2.1, 1.8, 1.6, 1.4, 1.2, 1.0, 0.8, 0.6, 0.4, 0.2]
random.shuffle(rez)

def adecv(cr):
    i = cr.id
    try:
        return rez[i-1]
    except IndexError:
        return 0.0
    except:
        print('E: index neașteptat: %s' % str(i))
        raise

def main():
    n = 30      # dimensiune cromozom
    m = 10      # dimensiune populație

    popu = pcrmz.PCrmz()
    # inițializare populație
    for i in range(m):
        popu.cr.append(crmz.CrmzCB(n))

    # afișare populație
    print('Cromozomi generați automat:')
    for c in popu.cr:
        print('%d: %s, coeficient de adecvare %f' % (c.id, c.sir(), adecv(c)))

    print('')
    print popu.sel(adecv, info=True)


if __name__ == '__main__':
    main()
