#!/bin/bash

cd ../fin_model_course
pipenv run python -m build_tools.gen_zipped_content
pipenv run python -m build_tools.gen_downloads_page
