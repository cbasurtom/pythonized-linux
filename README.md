# pythonized-linux

pythonized-linux is a repository dedicated to various Linux commands I have implemented into Python as practice, optional coursework for [Systems Programming](https://www3.nd.edu/~pbui/teaching/cse.20289.sp24/), and overall just for fun. These programs were essential for comprehending how to manage text input and output 

More commands to be included.

## cutit

### Usage

```python
'''Usage: cutit.py -d DELIMITER -f FIELDS

Print selected parts of lines from stream to standard output.

    -d DELIMITER    Use DELIM instead of TAB for field delimiter
    -f FIELDS       Select only these fields'''
```

## wcit

### Usage

```python
'''Usage: wcit.py [-l | -w | -c]

Print newline, word, and byte counts from standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, byte.

    -c      Print byte counts
    -l      Print newline counts
    -w      Print word counts'''
```

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
