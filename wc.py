#!/usr/bin/env python3

''' wc.py - print newline, word, and byte counts for stream '''

import io
import sys

# Functions

def usage(exit_status: int=0) -> None:
    ''' Print usage message and exit. '''
    print('''Usage: wc.py [-l | -w | -c]

Print newline, word, and byte counts from standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, byte.

    -c      Print byte counts
    -l      Print newline counts
    -w      Print word counts''', file=sys.stderr)
    sys.exit(exit_status)

def count_stream(stream=sys.stdin) -> dict[str, int]:
    ''' Count the newlines, words, and bytes in specified stream.

    >>> count_stream(io.StringIO('Despite all my rage, I am still just a rat in a cage'))
    {'newlines': 1, 'words': 13, 'bytes': 52}
    '''
    counts = {'newlines': 0, 'words': 0, 'bytes': 0}
    
    for line in stream:
        counts['words'] = int(counts.get('words', 0)) + len(line.split())
        counts['bytes'] = int(counts.get('bytes', 0)) + len(line)
        counts['newlines'] = int(counts.get('newlines', 0)) + 1

    return counts

def print_counts(counts: dict[str, int], options: list[str]) -> None:
    ''' Print the newline, word, and byte counts.  If none of the options are
    specified, then include all options in output.  Othewrise, only include the
    specified options.

    Note: always output the counts the following order: newlines, words, bytes.

    >>> print_counts({'newlines': 1, 'words': 13, 'bytes': 52}, ['newlines', 'words', 'bytes'])
    1 13 52
    '''
    result = ""

    if not options:
        options = ['newlines', 'words', 'bytes']

    if 'newlines' in options:
        result += str(counts.get('newlines')) + " "

    if 'words' in options:
        result += str(counts.get('words')) + " "

    if 'bytes' in options:
        result += str(counts.get('bytes')) + " "

    print(result.strip())

# Main Execution

def main(arguments=sys.argv[1:], stream=sys.stdin) -> None:
    ''' Print the newline, word, and byte counts from stream.

    This function will parse the command line arguments to select which counts
    to include in the final report.

    >>> main([], io.StringIO('Despite all my rage, I am still just a rat in a cage'))
    1 13 52
    '''
    options = []
    c = True
    
    # Parse command line arguments
    while arguments:
        argument = arguments.pop(0)
        if argument == '-h':
            usage(0)
        elif argument == '-c':
            options.append('bytes')
            c = False
        elif argument == '-l':
            options.append('newlines')
            c = False
        elif argument == '-w':
            options.append('words')
            c = False
        else:
            usage(1)
        
    if c:
        options = ['newlines', 'words', 'bytes']

    # Count stream and print counts
    counts = count_stream(stream)

    print_counts(counts, options)

if __name__ == '__main__':
    main()

# vim: set sts=4 sw=4 ts=8 expandtab ft=python:
