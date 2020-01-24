from typing import Sequence
from subprocess import run
from distutils.core import run_setup

import conf
import version


DISTRIBUTION_NAME = f'{conf.PACKAGE_NAME}-{version.__version__}'
DISTRIBUTION_PATH = f'dist/{DISTRIBUTION_NAME}.tar.gz'


def twine(main_command: str):
    command = f'twine {main_command} {DISTRIBUTION_PATH}'
    run(command, shell=True, check=True)


def upload_app(build_only: bool = False):
    run_setup('setup.py', script_args=['sdist', 'bdist_wheel'])
    if build_only:
        return
    twine('upload')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=f'Build and upload {conf.PACKAGE_NAME} to PyPi')
    parser.add_argument(
        '--build-only',
        action='store_true',
        help='Only build the package, do not upload'
    )

    args = parser.parse_args()

    upload_app(build_only=args.build_only)