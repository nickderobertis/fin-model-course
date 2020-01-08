#!/bin/bash
cd ..
mkdir -p docsrc/source/binder/
echo "$(python binder_requirements.py)" > docsrc/source/binder/requirements.txt
cd docsrc
