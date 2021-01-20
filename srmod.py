#!/usr/bin/env python3

import pysrt
from copy import copy, deepcopy

in_file = 'en_forced.srt'
sub = pysrt.open(in_file)

# starting index is 0 like everything else

sub[3].shift(seconds=+30.5)
n_subs = len(sub)

for i in range(4, n_subs, 1):
    sub[i].shift(seconds=-26)

sub[7].start += {'seconds': -2.5}

for i in range(8, n_subs, 1):
    sub[i].shift(seconds=-2)

sub[9].end += {'seconds': -1}

sub[10].shift(seconds=-.5)
sub[10].shift(seconds=-.2)

sub[11].end += {'seconds': -1}

for i in range(14, n_subs, 1):
    sub[i].shift(seconds=-0.5)

for i in range(23, n_subs, 1):
    sub[i].shift(seconds=-14.5)

for i in range(24, n_subs, 1):
    sub[i].shift(seconds=-1.1)

# subtitle 4 was part of the unwanted CG additions
del sub[3]

# index re-numbering is not automatic after del
sub.clean_indexes()
sub.save('new_' + in_file)

# Notes: copy is shallow vs deepcopy for objects but even a deepcopy will miss
# class methods.  Initializing object as follows will break the .clean_indexes()
#
# sub_c  = deepcopy(sub[:6])
#
# Using an empty srt file was the only clean way to initialize a new pysrt object
open('null.srt', 'a').close()
sub_c = pysrt.open('null.srt')

for in_sub in sub[:6]:
    sub_c.append(deepcopy(in_sub))

sub_c.append(deepcopy(sub[6]))
sub_c[6].end = deepcopy(sub_c[6].start)
sub_c[6].end += {'seconds': +4.2}
sub_c[6].text = 'This bounty hunter is my kind of scum...'
sub_c.append(deepcopy(sub[6]))
sub_c[7].start += {'seconds': 4.3}
sub_c[7].text = 'fearless and inventive.'
for in_sub in sub[7:]:
    sub_c.append(deepcopy(in_sub))

# index re-numbering is not automatic after new inserts
sub_c.clean_indexes()
sub_c.save('new2_' + in_file)