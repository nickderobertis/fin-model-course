import conf

if __name__ == '__main__':
    for package in conf.BINDER_ENVIRONMENT_REQUIRES:
        print(package)