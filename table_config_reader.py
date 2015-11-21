from configparser import ConfigParser

rbaus035 py1 57$ cat T
[tables]
numq=10
tables=3,4,6
rbaus035 py1 58$ mv T .tables
rbaus035 py1 59$ python3
ActivePython 3.3.2.0 (ActiveState Software Inc.) based on
Python 3.3.2 (default, Sep 16 2013, 23:12:56) 
[GCC 4.0.2 20051125 (Red Hat 4.0.2-8)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from configparser import ConfigParser
>>> cfg=ConfigParser()
>>> cfg.read('.tables')
['.tables']
>>> cfg
<configparser.ConfigParser object at 0x7f883e9a1bd0>
>>> cfg['tables']
<Section: tables>
>>> cfg.sections()
['tables']
>>> for k in cfg['tables']:
...     print(k)
... 
numq
tables
>>> cfg['tables']['numq']
'10'
>>> ^[[A
  File "<stdin>", line 1
    ^
SyntaxError: invalid syntax
>>> cfg['tables']['tables']
'3,4,6'
>>> quit()
rbaus035 py1 60$
