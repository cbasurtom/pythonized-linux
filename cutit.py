#!/usr/bin/env python3

''' cutit.py - remove sections from each line of stream '''

import io
import sys

# Functions

def usage(exit_status: int=0) -> None:
    ''' Print usage message and exit. '''
    print('''Usage: cutit.py -d DELIMITER -f FIELDS

Print selected parts of lines from stream to standard output.

    -d DELIMITER    Use DELIM instead of TAB for field delimiter
    -f FIELDS       Select only these fields''', file=sys.stderr)
    sys.exit(exit_status)

def strs_to_ints(strings: list[str]) -> list[int]:
    ''' Convert all strings in list to integers.

    >>> strs_to_ints(['2', '4'])
    [2, 4]
    '''
    int_list = []
    
    for num in strings:
        int_list.append(int(num))

    return int_list

def cut_line(line: str, delimiter: str='\t', fields: list[int]=[]) -> list[str]:
    ''' Return selected fields from line separated by delimiter.

    >>> cut_line('Harder, Better, Faster, Stronger', ',', [2, 4])
    [' Better', ' Stronger']
    '''
    
    del_line = line.split(delimiter)

    fin_line = []

    for num in fields:
        try:
            fin_line.append(del_line[int(num)-1])
        except IndexError:
            pass

    return fin_line

def cut_stream(stream=sys.stdin, delimiter: str='\t', fields: list[int]=[]) -> None:
    ''' Print selected parts of lines from stream to standard output.

    >>> cut_stream(io.StringIO('Harder, Better, Faster, Stronger'), ',', [2, 4])
     Better, Stronger
    '''

    for line in stream:
        line = line.rstrip()
        line = cut_line(line, delimiter, fields)
        curline = delimiter.join(line)
        print(curline)



# Main Execution

def main(arguments=sys.argv[1:], stream=sys.stdin) -> None:
    ''' Print selected parts of lines from stream to standard output.

    This function will parse the command line arguments to determine the
    delimiter and which fields to select from each line.

    >>> main('-d , -f 2,4'.split(), io.StringIO('Harder, Better, Faster, Stronger'))
     Better, Stronger
    '''

    # Display usage message if invalid input
    if len(arguments) < 1:
        usage(1)

    fields = []
    delimiter = '\t'

    # Parse command line arguments
    while arguments:
        argument = arguments.pop(0)
        if argument == '-h':
            usage(0)
        elif argument == '-f':
            nums = arguments.pop(0)
            fields = strs_to_ints(nums.split(','))
        elif argument == '-d':
            delimiter = arguments.pop(0)
        else:
            usage(1)

    if not fields:
        usage(1)

    # Cut stream with delimiter and fields
    cut_stream(stream, delimiter, fields)

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
