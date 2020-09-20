.. fin-model-course documentation master file, created by
   cookiecutter-pypi-sphinx.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Nick DeRobertis' Financial Modeling Course!
********************************************************************

A Python and Excel Financial Modeling Course

.. toctree::
   :caption: Course Content
   :maxdepth: 2
   {% for lecture_path in lecture_paths %}
   {{ lecture_path }}{% endfor %}



.. toctree::
   :caption: Course Resources
   :maxdepth: 2

   downloads