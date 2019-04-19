# code snippets

mylist = ['A','B','C','D']
for n,listitem in enumerate(mylist):
    print(n, listitem)

{L: n+1 for n, L in enumerate(chr(65+i) for i in range(5))}
      (output: {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5})
objects = []
with (open("myfile", "rb")) as openfile:
  while True:
      try:
          objects.append(pickle.load(openfile))
      except EOFError:
          break

from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
     d[k] += 1

d.items() # output: [('i', 4), ('p', 2), ('s', 4), ('m', 1)]


def distance(p1, p2) :
    (sum((wi - vi)**2 for  in zip(p1, p2)))**.5
print distance((0,0,0), (5,4,3))


import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
'Hello world!'


blocks = []
for block in iter(partial(f.read, 32), '')
 nblocks.append(block)
 
# items() returns key value pair list
for a_key, a_value in my_dictionary.items():
    print a_key, '-->', a_value

# iteritems() returns key value pair iterable
for a_key, a_value in my_dictionary.iteritems():
    print a_key, '-->', a_value

a = ['mine', 'his', 'hers']
b = ['x', 'y', 'z']
dictionary = dict(izip(a,b))

colors = ['red', 'green', 'red', 'green', 'blue', 'green', 'red']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
# better: use the get method on dictionaries
d = {}
for color in colors
    d[color] = d.get(color, 0) + 1
