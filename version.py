import conf
major, minor, release = conf.PACKAGE_VERSION_TUPLE
__version__ = f"{major}.{minor}.{release}"
__version_info__ = conf.PACKAGE_VERSION_TUPLE

if __name__ == '__main__':
    print(__version__)