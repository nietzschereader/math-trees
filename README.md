# Math Trees

Make math expressions with trees


## Getting Started
```
    git clone https://github.com/spboyle/math-trees`
    cd math-trees
    pip install -r requirements_dev.txt
    python setup.py develop
```

### Running tests
`python setup.py test`


## Code Challenge
Please code the following. Feel free to add to or re-structure the project as needed.
* Create a math syntax tree which can represent math expressions that supports the following:
  * Real numbers
  * plus(+)
  * minus(-)
  * times(*)
  * divide(/)
* Implement an evaluation method which calculates the value of the expression
* Write a parser which converts an ascii string to tree format
* Implement a `__str__` method which converts a math tree into an ascii string equivalent
* Make the string parser handle parentheses ()


Please dedicate about two to four hours on this -- complete as much as you are able, but don't feel that you have to complete every bullet. They are ordered by priority, so we suggest coding to each requirement in top-down order.


## Credits
This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
