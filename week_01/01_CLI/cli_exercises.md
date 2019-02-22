# Fundamentals Exercise 1: CLI

Perform the following tasks using the CLI and copy and paste
the commands and results below.

- Navigate to your home directory
- Create a new directory called CodingNomads. We will use this folder
to house materials for the course.
- Move into the CodingNomads folder
- Create new folder cli_testing
- Inside of folder cli_testing,
    a. print the directory path
    b. create 3 new .txt files all with different names (file1.txt,
    file2.txt, file3.txt)
    c. list the contents of the folder
    d. rename one of the files
- Inside of folder cli_testing, create a new folder
- Copy a file from cli_testing to the new folder
- Move a different file from cli_testing to the new folder
- Demonstrate removing:
    a. A file
    b. A folder
```bash
MacBook-Air-Katarzyna-2% pwd      
/Users/Blake/Documents/learning/python-onsite/week_01
MacBook-Air-Katarzyna-2% ..
zsh: permission denied: ..
MacBook-Air-Katarzyna-2% ~
zsh: permission denied: /Users/Blake
MacBook-Air-Katarzyna-2% cd ..
MacBook-Air-Katarzyna-2% pwd
/Users/Blake/Documents/learning/python-onsite
MacBook-Air-Katarzyna-2% cd ..
MacBook-Air-Katarzyna-2% pwd
/Users/Blake/Documents/learning
MacBook-Air-Katarzyna-2% cd ..
MacBook-Air-Katarzyna-2% pwd
/Users/Blake/Documents
MacBook-Air-Katarzyna-2% cd..
zsh: command not found: cd..
MacBook-Air-Katarzyna-2% cd ..
MacBook-Air-Katarzyna-2% pwd
/Users/Blake
MacBook-Air-Katarzyna-2% mkdir codingnomads
MacBook-Air-Katarzyna-2% pwd
/Users/Blake
MacBook-Air-Katarzyna-2% cd codingnomads
MacBook-Air-Katarzyna-2% mdkri cli_testing
zsh: command not found: mdkri
MacBook-Air-Katarzyna-2% mkdir cli_testing
MacBook-Air-Katarzyna-2% cd cli_testing
MacBook-Air-Katarzyna-2% print(cd)
zsh: number expected
MacBook-Air-Katarzyna-2% print(pwd)
zsh: number expected
MacBook-Air-Katarzyna-2% pwd
/Users/Blake/codingnomads/cli_testing
MacBook-Air-Katarzyna-2% touch file1.txt
MacBook-Air-Katarzyna-2% touch file2.txt 
MacBook-Air-Katarzyna-2% touch file3.txt
MacBook-Air-Katarzyna-2% ls -la
total 0
drwxr-xr-x  5 Blake  staff  170 Feb 22 15:46 .
drwxr-xr-x  3 Blake  staff  102 Feb 22 15:43 ..
-rw-r--r--  1 Blake  staff    0 Feb 22 15:45 file1.txt
-rw-r--r--  1 Blake  staff    0 Feb 22 15:45 file2.txt
-rw-r--r--  1 Blake  staff    0 Feb 22 15:46 file3.txt
MacBook-Air-Katarzyna-2% mv file3.txt file4.txt
MacBook-Air-Katarzyna-2% ls    
file1.txt       file2.txt       file4.txt
MacBook-Air-Katarzyna-2% mkdir new_folder
MacBook-Air-Katarzyna-2% ls
file1.txt       file2.txt       file4.txt       new_folder
MacBook-Air-Katarzyna-2% mv file1.txt new_folder
MacBook-Air-Katarzyna-2% ls
file2.txt       file4.txt       new_folder
MacBook-Air-Katarzyna-2% mv file2.txt new_folder
MacBook-Air-Katarzyna-2% ls
file4.txt       new_folder
MacBook-Air-Katarzyna-2% mv file4.txt new_folder
MacBook-Air-Katarzyna-2% cd new_folder
MacBook-Air-Katarzyna-2% mv file4.txt ..    
MacBook-Air-Katarzyna-2% cd cli_testing
cd: no such file or directory: cli_testing
MacBook-Air-Katarzyna-2% cd
MacBook-Air-Katarzyna-2% ls
Applications                    Downloads                       Music                           Public                          gekko
Desktop                         Library                         Pictures                        PycharmProjects                 java_error_in_pycharm.hprof
Documents                       Movies                          PlayOnMac's virtual drives      codingnomads                    newdir
MacBook-Air-Katarzyna-2% cd newdir
MacBook-Air-Katarzyna-2% pwd
/Users/Blake/newdir
MacBook-Air-Katarzyna-2% cd cli_testing
cd: no such file or directory: cli_testing
MacBook-Air-Katarzyna-2% ls
MacBook-Air-Katarzyna-2% cd ..       
MacBook-Air-Katarzyna-2% cd codingnomads
MacBook-Air-Katarzyna-2% ls
cli_testing
MacBook-Air-Katarzyna-2% cd cli_testing
MacBook-Air-Katarzyna-2% ls
file4.txt       new_folder
MacBook-Air-Katarzyna-2% cp file4.txt new_folder
MacBook-Air-Katarzyna-2% cd new_folder
MacBook-Air-Katarzyna-2% ls
file1.txt       file2.txt       file4.txt
MacBook-Air-Katarzyna-2% rv file1.txt
zsh: command not found: rv
MacBook-Air-Katarzyna-2% rm file1.txt
MacBook-Air-Katarzyna-2% ls
file2.txt       file4.txt
MacBook-Air-Katarzyna-2% ls
file2.txt       file4.txt
MacBook-Air-Katarzyna-2% cd..
zsh: command not found: cd..
MacBook-Air-Katarzyna-2% cd ..
MacBook-Air-Katarzyna-2% mkdir target_folder
MacBook-Air-Katarzyna-2% ls
file4.txt       new_folder      target_folder
MacBook-Air-Katarzyna-2% rm -rf target_folder
MacBook-Air-Katarzyna-2% ls
file4.txt       new_folder

```

## vim

- Use `$ vim` to write some text inside a file
- Use `$ cat` print contents of file
- Use `$ grep` to search for a word inside file


## explore advanced CLI

- What is the difference between the two commands > and >>?
- Create a file hello.txt with the text "how?!", then append the text
    to another file called my_file.txt
- Overwrite the content of my_file.txt with "tell me"
