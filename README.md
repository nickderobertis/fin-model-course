
[![](https://codecov.io/gh/nickderobertis/fin-model-course/branch/master/graph/badge.svg)](https://codecov.io/gh/nickderobertis/fin-model-course)

# fin-model-course

## Overview

A Python and Excel Financial Modeling Course

## Getting Started

Clone or download and extract the repo. Get a 
terminal inside the main repo folder.

If you do not have `pipenv` installed, run:

```
pip install pipenv
```

To set up the environment, run:

```
pipenv sync
```

## File Layout

### Lectures and Documents

This project uses [`pl-builder`](
https://github.com/nickderobertis/pl-builder/
), to build [`py-ex-latex`](https://nickderobertis.github.io/py-ex-latex/) documents so the lecture sources are 
in `fin_model_course/plbuild/sources/presentation`
and the document sources are in 
`fin_model_course/plbuild/sources/document`.

After building, the generated LaTeX and PDFs will be
in `fin_model_course/Documents`, 
`fin_model_course/Slides` (presentation version),
and `fin_model_course/Handouts` (static version of slides).

## Useful Scripts

> Note: all scripts should be run within the `pipenv` environment. 
> Either prefix all commands with `pipenv run ` or once run
> `pipenv shell` to get a shell with the `pipenv` environment.
> If you're in the `pipenv shell`, no need to prefix commands.

> Note: Run commands from within the `fin_model_course` folder

### Build Slides and Documents

#### Build All

Run `plbuilder build`

> Note: This will take a while!

#### Build Single

Use the `build` command of `plbuilder` with the file path, e.g.:

```
plbuilder build plbuild/sources/presentation/1_intro.py
```

#### Auto-build

To automatically build sources whenever they are updated,
run `plbuilder autobuild`.

> Note: This will not notice when you change some 
> file which is imported by the source rather than
> the source itself. It only monitors for direct 
> changes to the source files.
 

## Links

See the
[course site here.](
https://nickderobertis.github.io/fin-model-course/
)
