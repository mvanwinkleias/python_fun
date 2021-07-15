#!/usr/bin/python3

import sys
import contextlib

# How does one choose between opening a list of files passed in as
# arguments, or if no files are passed in, then use STDIN?
#
# How does one choose between opening an output file, or if
# no output file was given, then output to stdout?
#
# This was borrowed from https://stackoverflow.com/a/29824059
#	( https://stackoverflow.com/users/1165181/bryant1410 )
# ... which was borrowed from https://stackoverflow.com/a/17603000/874188
#	( https://stackoverflow.com/users/54017/wolph )
#
# It might be overkill for simply opening a specified file, but
# it does show how to iterate through multiple files that might
# have been passed in as arguments.  I wouldn't nest too deeply with it
# nor would I use it for anything that's VERY serious.
#
# It has been tested on python2 and python3.
#
# The comments for the second borrowed link are below.  I havent tested
# the usage with the borrowed modification, but it looks like it
# still should work...
#
#	# For Python 2 you need this line
#	from __future__ import print_function
#
# 	# writes to some_file
#	with smart_open('some_file') as fh:
#		print('some output', file=fh)
#
# 	# writes to stdout
#	with smart_open() as fh:
#		print('some output', file=fh)
#
#	# writes to stdout
#		with smart_open('-') as fh:
#		print('some output', file=fh)

@contextlib.contextmanager
def _contrived_open(filename, mode='Ur'):
    if filename == '-':
        if mode is None or mode == '' or 'r' in mode:
            fh = sys.stdin
        else:
            fh = sys.stdout
    else:
        fh = open(filename, mode)
    try:
        yield fh
    finally:
        if filename != '-':
            fh.close()

# do_stuff just assumes that it's a file that's meant to be read from
# and it sends the output to stdout.    
def do_stuff(handle):
	while True:
		line = handle.readline()
		if not line:
			break
		# Print seems to insert extra newlines...
		# print(line)

		sys.stdout.write(line)

if __name__ == '__main__':
    args = sys.argv[1:]
    if args == []:
        args = ['-']
    for filearg in args:
        with _contrived_open(filearg) as handle:
            do_stuff(handle)

