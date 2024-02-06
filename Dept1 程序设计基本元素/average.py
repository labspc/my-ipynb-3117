#-----------------------------------------------------------------------
# average.py
# https://introcs.cs.princeton.edu/python/15inout/average.py.html
#-----------------------------------------------------------------------

import stdio

# Read floats from the standard input stream until end-of-file.
# Write to standard output the average of those floats.

total = 0.0
count = 0
while not stdio.isEmpty():
    value = stdio.readFloat()
    total += value
    count += 1
avg = total / count
stdio.writeln('Average is ' + str(avg))

#-----------------------------------------------------------------------
