'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''


def sed (pattern_str, replace_string, filename1, filename2):
    with open(filename1) as file_object:
        contents = file_object.readlines()
        filename = filename2
        with open(filename, 'w') as file_object1:
            for line in contents:
                file_object1.write(line)
                if pattern_str in filename1:
                    newline = line.replace(pattern_str, replace_string)
                    file_object1.write(newline)
