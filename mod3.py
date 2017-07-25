Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a="Meet"
>>> b="meet"
>>> c="Meat"
>>> a==b
False
>>> a==b
False
>>> b==c
False
>>> a!=b
True
>>> my_string"bananayellowthinkhatgreyBIGcalifornia314"
SyntaxError: invalid syntax
>>> my_string"bananayellowthinkhatgreyBIGcalifornia314"
SyntaxError: invalid syntax
>>> my_string
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    my_string
NameError: name 'my_string' is not defined
>>> my_string="bananayellowthinkhatgreyBIGcalifornia314"
>>> meet_value=(12:17)
SyntaxError: invalid syntax
>>> my_string=(12:17)
SyntaxError: invalid syntax
>>> my_string[12:17]
'think'
>>> meet_value[12:17]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    meet_value[12:17]
NameError: name 'meet_value' is not defined
>>> my_string[12:17],[25:28]
SyntaxError: invalid syntax
>>> my_string[12:17]+[25:28]
SyntaxError: invalid syntax
>>> my_string[12:17]+my_string[25:28]
'thinkIGc'
>>> my_string[12:17]+" "+my_string[24:27]
'think BIG'
>>> 
my_string.upper()
'BANANAYELLOWTHINKHATGREYBIGCALIFORNIA314'
>>> 'BANANAYELLOWTHINKHATGREYBIGCALIFORNIA314'
'BANANAYELLOWTHINKHATGREYBIGCALIFORNIA314'
>>> meet_value=my_string[12:17]+" "+my_string[24:27]
>>> meet_value.upper()
'THINK BIG'
>>> 
