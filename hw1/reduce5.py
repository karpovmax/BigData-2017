#!/usr/bin/env python
# coding=utf-8
import sys
current_elem = None
current_sum = 0.0
current_count = 0
elem = None

for line in sys.stdin:
    line = line.strip()
    params = line.split('\t')
    antiNucleus = int(params[0])
    Pt = float(params[1])
    elem = antiNucleus
    if current_elem == elem:
        current_count += 1
        current_sum += Pt
    else:
        if current_elem is not None:
            mean = current_sum / current_count
            print ('%s\t%s\t%s' % (str(current_elem), str(mean), 'mean'))
        current_sum = Pt
        current_count = 1
        current_elem = elem

if current_elem == elem:
    mean = current_sum / current_count
    print ('%s\t%s\t%s' % (str(current_elem), str(mean), 'mean'))
