introduction and setup
===
# introduction
today's workshop is very simple. we will be
- defining how we will work on these exercises
- checking whether participants have the prerequisites
- install prerequisites as necessary
- test project: fetch a list of files in a directory
 
# what is this all about
the purpose of these exercises is to provide a venue for data science team members to help each other develop the necessary python skills and hopefully out outgrow them and have fun with python. we should be learning something useful and/or interesting each time.

we will be helping each other learn. there is no sage on this stage, but a guide to the side. i am no python expert

# installing prerequisites

- there are [instructions for installing python 3.7 here](https://www.python.org/downloads/)
- there are [instructions for installing jupyter here](https://jupyter.org/install)

```
sudo easy_install pip
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
jupyter notebook
```

# test 
## do this
- write a python function that takes no arguments, but will read the files in the current working directory and return a list of them. test it while in a couple of directories.
- edit that code to take in two arguments, one for the directory and another for the file extension pattern. test it.

## note:
- there are multiple ways to do this, a simple one utilises the `os` module. (`import os`)
- `'.'` refers to the current directory. `'~/' is your user's home directory`
- `os.path.exists`
- `os.path.isfile`
- `os.path.isdir`
- `os.getcwd()`
- `os.listdir('.')`


# exercise
- set up your machine
- get this git archive
- make a new subfolder under `solutions/` called 'ab' where 'ab' are your initials
- 
branch 'exercise01_AB', where AB are your initials
- solve this problem 
