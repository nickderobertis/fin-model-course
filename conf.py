# This is the main settings file for package setup and PyPi deployment.
# Sphinx configuration is in the docsrc folder

# Main package name
PACKAGE_NAME = "fin_model_course"

# Name of Repo
REPO_NAME = "fin-model-course"

# Github username of the user which owns the repo
REPO_USERNAME = "nickderobertis"

# List of maintainers of package, by default the same user which owns the repo
# Pull requests raised by these maintainers without the "no auto merge" label will be automatically merged
REPO_MAINTAINERS = [
    REPO_USERNAME,
]

# Package version in the format (major, minor, release)
PACKAGE_VERSION_TUPLE = (0, 1, 10)

# Short description of the package
PACKAGE_SHORT_DESCRIPTION = "A Python and Excel Financial Modeling Course"

# Long description of the package for PyPI
# Set to 'auto' to use README.md as the PyPI description
# Any other string will be used directly as the PyPI description
PACKAGE_DESCRIPTION = 'auto'

# Author
PACKAGE_AUTHOR = "Nick DeRobertis"

# Author email
PACKAGE_AUTHOR_EMAIL = "whoopnip@gmail.com"

# Name of license for package
PACKAGE_LICENSE = 'MIT'

# Classifications for the package, see common settings below
PACKAGE_CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

# Add any third party packages you use in requirements here
PACKAGE_INSTALL_REQUIRES = [
    # Include the names of the packages and any required versions in as strings
    # e.g.
    # 'package',
    # 'otherpackage>=1,<2'
]

# Add any third party packages you use in requirements for optional features of your package here
# Keys should be name of the optional feature and values are lists of required packages
# E.g. {'feature1': ['pandas', 'numpy'], 'feature2': ['matplotlib']}
OPTIONAL_PACKAGE_INSTALL_REQUIRES = {

}

# Packages added to Binder environment so that examples can be executed in Binder
# By default, takes this package (PACKAGE_NAME)
# everything the package requires (PACKAGE_INSTALL_REQUIRES) and everything
# that the package optionally requires (OPTIONAL_PACKAGE_INSTALL_REQUIRES) and adds them all to one list
# If a custom list is passed, it must include all the requirements for the Binder environment
BINDER_ENVIRONMENT_REQUIRES = list(
    set(
        PACKAGE_INSTALL_REQUIRES + [PACKAGE_NAME] +
        [package for package_list in OPTIONAL_PACKAGE_INSTALL_REQUIRES.values() for package in package_list]
    )
)


# Sphinx executes all the import statements as it generates the documentation. To avoid having to install all
# the necessary packages, third-party packages can be passed to mock imports to just skip the import.
# By default, everything in PACKAGE_INSTALL_REQUIRES will be passed as mock imports, along with anything here.
# This variable is useful if a package includes multiple packages which need to be ignored.
DOCS_OTHER_MOCK_IMPORTS = [
    # Include the names of the packages as they would be imported, e.g.
    # 'package',
]

# Add any Python scripts which should be exposed to the command line in the format:
# CONSOLE_SCRIPTS = ['funniest-joke=funniest.command_line:main']
CONSOLE_SCRIPTS = [],

# Add any arbitrary scripts to be exposed to the command line in the format:
# SCRIPTS = ['bin/funniest-joke']
SCRIPTS = []

# Optional Google Analytics tracking ID for documentation
# Go to https://analytics.google.com/ and set it up for your documentation URL
# Set to None or empty string to not use this
GOOGLE_ANALYTICS_TRACKING_ID = "UA-155751319-1"

PACKAGE_URLS = {
    'Code': f'https://github.com/{REPO_USERNAME}/{REPO_NAME}',
    'Documentation': f'https://{REPO_USERNAME}.github.io/{REPO_NAME}'
}

# Does not affect anything about the current package. Simply used for tracking when this repo was created off
# of the quickstart template, so it is easier to bring over new changes to the template.
_TEMPLATE_VERSION_TUPLE = (0, 5, 3)

if __name__ == '__main__':
    # Store config as environment variables
    env_vars = dict(locals())
    # Imports after getting locals so that locals are only environment variables
    import shlex
    for name, value in env_vars.items():
        quoted_value = shlex.quote(str(value))
        print(f'export {name}={quoted_value};')
