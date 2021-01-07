#!/usr/bin/env python3

import pysrt

in_file = 'en_forced.srt'
sub = pysrt.open(in_file)

# starting index is 0 like everything else

# del sub[3]
# index renumbering is not automatic after del
# sub.clean_indexes()

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

sub.save('new_' + in_file)