# Contributing (more like dev standards bc this is closed source)

## Formatting

* Follow PEP 8. That means:
  * Module, class, functions should be docstringed
  * Other PEP 8 things
  * Typing, import typing if neccesary for stuff like lists for mypy to calm down
* Use the Black formatter for python
* Run black with "black ." or install the pre-commit hook in utils

## Extentions for VS Code

* Python Intellisense - General thingy
* Pylint - PEP 8
  * "pylint.args": ["load-plugins=pylint_django"] <- add this to your settings.json for vs code
* Black Formatting for Python - Formatter
* AutoDocString -  For functions and classes
* Pylance - more python
* MyPy - Type checking
* iSort - Sorting stuff

## Venv

* Rember to use venv!
