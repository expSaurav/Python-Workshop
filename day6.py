Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
firstName="Saurav"
lastName="Suman"
full_name=firstName+lastName
firstName[0:7]
'Saurav'
lastName[0:6]
'Suman'
firstName[-7:-1]
'Saura'
firstName[-8:-1]
'Saura'
lastName[-1]
'n'
for i in range(0,len(full_name)+1,1):
    print(full_name[i])

    
S
a
u
r
a
v
S
u
m
a
n
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    print(full_name[i])
IndexError: string index out of range
for i in range(len(full_name),0,-1):
    print(full_name[i])

    
Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    print(full_name[i])
IndexError: string index out of range
for i in range(-1,0,-1):
    print(full_name[i])

    

for i in range(len(full_name)-1, -1, -1):
    print(full_name(i))

    
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    print(full_name(i))
TypeError: 'str' object is not callable
for i in range(len(full_name)-1, -1, -1):
    print(full_name[i])

    
n
a
m
u
S
v
a
r
u
a
S
'''list'''
'list'
countries=['india','australia','pakistan']
countries
['india', 'australia', 'pakistan']
countries.add('belgium')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    countries.add('belgium')
AttributeError: 'list' object has no attribute 'add'
countries.append('belgium')
countries
['india', 'australia', 'pakistan', 'belgium']
countries.append(4,'bhutna')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    countries.append(4,'bhutna')
TypeError: list.append() takes exactly one argument (2 given)
countries.insert(4,'bhutan')
countries
['india', 'australia', 'pakistan', 'belgium', 'bhutan']
countries[-1]
'bhutan'
countries[0:3]
['india', 'australia', 'pakistan']
mixed_list=[1,2,'india',4.5,True]
mixed_list[0]='pak'
mixed_list
['pak', 2, 'india', 4.5, True]
mixed_list.pop()
True
mixed_list
['pak', 2, 'india', 4.5]
mixed_list.remove(2)
mixed_list
['pak', 'india', 4.5]
counties
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    counties
NameError: name 'counties' is not defined. Did you mean: 'countries'?
countries
['india', 'australia', 'pakistan', 'belgium', 'bhutan']
countries.pop(2)
'pakistan'
del mixed_list[0]
mixed_list
['india', 4.5]
for country in countries:
    print(country)

    
india
australia
belgium
bhutan
for index, country in enumerate(countries):
    print(f"Index: {index}, country: {country}")

    
Index: 0, country: india
Index: 1, country: australia
Index: 2, country: belgium
Index: 3, country: bhutan
countries
['india', 'australia', 'belgium', 'bhutan']
countries.reverse()
countries
['bhutan', 'belgium', 'australia', 'india']
countries.index(belgium)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    countries.index(belgium)
NameError: name 'belgium' is not defined
countries.index('belgium')
1
full_name[0]='k'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    full_name[0]='k'
TypeError: 'str' object does not support item assignment
mySet={1,2,3,4}
newSet={4,3,2,1}
mySet=newSet
mySet
{1, 2, 3, 4}
newSet
{1, 2, 3, 4}
mySet={4,3,2,1}
mySet==newSet
True
mySet
{1, 2, 3, 4}
newSet
{1, 2, 3, 4}
mySet={8,4,5,6}
mySet
{8, 4, 5, 6}
newSet={4,5,6,8}
mySet==newSet
True
myset.add(1)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    myset.add(1)
NameError: name 'myset' is not defined. Did you mean: 'mySet'?
mySet.add(1)
mySet
{1, 4, 5, 6, 8}
mySet.remove(8)
mySet
{1, 4, 5, 6}
mySet.discard()
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    mySet.discard()
TypeError: set.discard() takes exactly one argument (0 given)
mySet.discard(0)
mySet
{1, 4, 5, 6}
mySet.clear()
mySet
set()
mySet.add(5)
mySet.pop()
5
mySet
set()
t=(1,'saurav
   
SyntaxError: unterminated string literal (detected at line 1)
tpl=(1,'Saurav',2,5.4,False)
   
tpl
   
(1, 'Saurav', 2, 5.4, False)
tpl[0]
   
1
'''tpl is imuutable'''
   
'tpl is imuutable'
'''set is mutable'''
   
'set is mutable'
type(tpl)
   
<class 'tuple'>
typle(countries)
   
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    typle(countries)
NameError: name 'typle' is not defined. Did you mean: 'tuple'?
type(countries)
   
<class 'list'>
type(mySet)
   
<class 'set'>
new_tuple=1,2,3
   
type(new_tuple)
   
<class 'tuple'>
tpl[1]
   
'Saurav'
tpl[1]='hi'
   
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    tpl[1]='hi'
TypeError: 'tuple' object does not support item assignment
tpl2=1,1,1,1,1,4,3,2,4
   
tpl2.count(2)
   
1
tpl2.count(1)
   
5
tpl2.index(1)
   
0
tpl3=1,2,3
   
a,b,c=tpl3
   
a
   
1
b
   
2
c
   
3
a,b,c
   
(1, 2, 3)
type(a,b,c)
   
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    type(a,b,c)
TypeError: type.__new__() argument 1 must be str, not int
student={'name':'Saurav', 'Age':18, 'Roll_nu':1}
   
student
   
{'name': 'Saurav', 'Age': 18, 'Roll_nu': 1}
type(student)
   
<class 'dict'>
del student[name]
   
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    del student[name]
NameError: name 'name' is not defined


'Saurav
   
SyntaxError: unterminated string literal (detected at line 1)

'Saurav' in student
   
False
'name' in student
   
True
'Saurav' in student[name]
   
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    'Saurav' in student[name]
NameError: name 'name' is not defined
'''function'''
   
'function'
def add(a,b):
    return a+b
add(4,5)
SyntaxError: invalid syntax
add(4,5)
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    add(4,5)
NameError: name 'add' is not defined
>>> def name():
...     print("Saurav")
... 
...     
>>> name()
Saurav
>>> result = add(4,5)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    result = add(4,5)
NameError: name 'add' is not defined
>>> a=4
>>> b=5
>>> add(a,b)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    add(a,b)
NameError: name 'add' is not defined
>>> def sub(a, b):
...     return a-b
... 
>>> sub(5,4)
1
>>> sub._doc_
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    sub._doc_
AttributeError: 'function' object has no attribute '_doc_'. Did you mean: '__doc__'?
>>> sub.__doc__
>>> print(sub.__doc__)
None
>>> 
