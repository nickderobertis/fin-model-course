# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = fin_model_course
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

autodoc:
	@sphinx-apidoc -M -o ./source/api -t ./apidoc/templates "../$(SPHINXPROJ)"

cleandoc:
	@rm -rf ./source/api
	@rm -rf ./source/stubs
	@rm -rf ./build
	@rm -rf ./source/auto_examples
	@rm -rf ../_examples
	@rm -rf ./source/binder/requirements.txt
	@rm -rf ./source/_static/generated
	@rm -rf ./source/lectures
	@rm -rf ./source/downloads.rst

github:
	@make cleandoc
	@./binder_requirements.sh
	@./nb-examples.sh
	@./gen-pdfs.sh
	@./gen-metadata.sh
	@./gen-lectures.sh
	@./gen-downloads.sh
	@make doctest
	@make autodoc
	@make html
	@cp -a build/html/. ../docs

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

