#-----------------------------------------------------------------------
# useargument.py
#-----------------------------------------------------------------------
import sys
import stdio # https://introcs.cs.princeton.edu/python/code/stdio.py

# Accept a name as a command-line argument. Write a message containing
# that name to standard output.

stdio.write('Hi, ')
stdio.write(sys.argv[1])
stdio.writeln('. How are you?')

#-----------------------------------------------------------------------

# python useargument.py Alice
# Hi, Alice. How are you?

# python useargument.py Bob
# Hi, Bob. How are you?

# python useargument.py Carol
# Hi, Carol. How are you?


# Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
# Last updated: Fri Oct 20 20:45:16 EDT 2017.
# https://introcs.cs.princeton.edu/python/11hello/useargument.py.html