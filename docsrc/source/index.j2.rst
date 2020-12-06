.. fin-model-course documentation master file, created by
   cookiecutter-pypi-sphinx.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Nick DeRobertis' Financial Modeling Course!
********************************************************************

This is the website for Nick DeRobertis' Financial Modeling courses.
Currently there are two courses: Financial Modeling with Python and
Excel and Advanced Financial Modeling with Python.

Financial Modeling with Python and Excel is targeted at students who
want to learn financial modeling and have
basic finance, accounting, and Excel knowledge, but no knowledge
of Python.

Advanced Financial Modeling with Python is meant for those who
are comfortable with financial modeling in Python but want to
learn more advanced topics. Completion of the Financial
Modeling with Python and Excel course would be good preparation
for this course.

If you like the courses and would like to be notified about future
updates, please
`subscribe to my YouTube channel <https://www.youtube.com/channel/UCu1oQ6zOiJtlJZ7GNivPPOg?sub_confirmation=1>`_.

{% for title, lecture_paths in all_lecture_paths.items() %}
.. toctree::
   :caption: {{ title }}
   :maxdepth: 2
   {% for lecture_path in lecture_paths %}
   {{ lecture_path }}{% endfor %}


{% endfor %}

.. toctree::
   :caption: Course Resources
   :maxdepth: 2

   downloads