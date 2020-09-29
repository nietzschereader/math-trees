Math Trees
==========
Make math expressions with trees


Getting Started
---------------
```
    git clone https://github.com/spboyle/math-trees`
    cd math-trees
    pip install -r requirements_dev.txt
    python setup.py develop
```

Running tests
~~~~~~~~~~~~~
`python setup.py test` or `pytest`


Code Challenge
--------
* Create a math syntax tree which can represent math expressions using numbers and the operations plus(+), minus(-), times(*), and divide(/)
* Implement an evaluation method which calculates the value of the expression
* Write a parser which converts an ascii string to tree format
  * BONUS: Make the parser handle parentheses ()
* Implement a `__str__` method which converts a math tree into an ascii string equivalent

A couple starter tests have been provided as a guide. Feel free to change or add to them as needed!


Credits
-------
This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
