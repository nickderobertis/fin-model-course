#!/bin/bash
cd ..
cp -R examples _examples
python ./nbexamples/ipynb_to_gallery.py ./nbexamples/ --out-folder ./_examples --replace
cd docsrc
