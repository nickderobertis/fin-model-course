"""Convert jupyter notebook to sphinx gallery notebook styled examples.
Usage: python ipynb_to_gallery.py <notebook.ipynb>
Dependencies:
pypandoc: install using `pip install pypandoc`
"""
import os
from typing import Optional

import pypandoc as pdoc
import json


def convert_ipynb_to_gallery(file_path: str, out_path: Optional[str] = None):
    if out_path is None:
        out_path = file_path.replace('.ipynb', '.py')

    python_file = ""

    nb_dict = json.load(open(file_path))
    cells = nb_dict['cells']

    for i, cell in enumerate(cells):
        if i == 0:
            assert cell['cell_type'] == 'markdown', \
                'First cell has to be markdown'

            md_source = ''.join(cell['source'])
            rst_source = pdoc.convert_text(md_source, 'rst', 'md')
            python_file = '"""\n' + rst_source + '\n"""'
        else:
            if cell['cell_type'] == 'markdown':
                md_source = ''.join(cell['source'])
                rst_source = pdoc.convert_text(md_source, 'rst', 'md')
                commented_source = '\n'.join(['# ' + x for x in
                                              rst_source.split('\n')])
                python_file = python_file + '\n\n\n' + '#' * 70 + '\n' + \
                    commented_source
            elif cell['cell_type'] == 'code':
                source = ''.join(cell['source'])
                python_file = python_file + '\n' * 2 + source

    python_file = python_file.replace("\n%", "\n# %")
    with open(out_path, 'w') as f:
        f.write(python_file)


def convert_all_in_folder_to_gallery(folder: str, out_folder: Optional[str] = None, replace: bool = False):
    folder = os.path.normpath(folder)

    if out_folder is None:
        out_folder = folder
    else:
        out_folder = os.path.normpath(out_folder)

    for path, folders, files in os.walk(folder):
        if '.ipynb_checkpoints' in path:
            # Skip checkpoints folders
            continue
        sub_path = os.path.sep.join(path.split(os.path.sep)[1:])  # relative path within folder
        current_out_folder = os.path.join(out_folder, sub_path)
        print(f'Outputting contents of {sub_path} to {current_out_folder}')
        if not os.path.exists(current_out_folder):
            os.makedirs(current_out_folder)
        files = [file for file in files if file.lower().endswith('ipynb')]
        for file in files:
            file_path = os.path.join(path, file)
            out_file = file.lower().replace('.ipynb', '.py').replace(' ', '_')
            out_path = os.path.join(current_out_folder, out_file)
            if not replace and os.path.exists(out_path):
                print(f'Skipping file {file} as .py already exists')
                continue
            print(f'Converting file {file}')
            convert_ipynb_to_gallery(file_path, out_path)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('folder',
                        help='Folder to convert ipynb to Sphinx Gallery py')
    parser.add_argument('-o', '--out-folder', default=None,
                        help='Output folder for Sphinx Gallery py files, default in same folder')
    parser.add_argument('-r', '--replace', action='store_true',
                        help='Overwrite existing Sphinx Gallery py files')
    args = parser.parse_args()
    convert_all_in_folder_to_gallery(args.folder, args.out_folder, args.replace)
