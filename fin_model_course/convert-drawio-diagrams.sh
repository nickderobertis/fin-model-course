#!/bin/bash
# Note: run from fin_model_course directory

for file in pltemplates/drawio_diagrams/*
do
  # Get new file path
  stripped_file=${file%.dio};
  filename=${stripped_file##*/}
  pdf_filename="plbuild/assets/images/$filename.pdf"

  echo "Converting $file to $pdf_filename";
  # Convert dio to pdf using drawio
  drawio -x --crop -f pdf -o $pdf_filename $file
done;