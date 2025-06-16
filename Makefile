SHELL=/bin/bash

CONTENT_PATH = content/
BUILD_PATH = _build/
SCRIPT_PATH = src/
STRUCTURE_PATH = ./data/structure.yaml
ROOT = livro
ROOT_DOC = index.md
.PHONY: all clean pdf toc structure build

toc:
	echo "Generating table of contents..."
	python  ${SCRIPT_PATH}make_toc.py --root=$(ROOT_DOC) --base-dir=${CONTENT_PATH}
	echo "Table of contents generated at ${CONTENT_PATH}_toc.yml"

build:
	echo "Building the book..."
	@jupyter-book build ${CONTENT_PATH} --path-output ${BUILD_PATH}

pdf:
	echo "Building the PDF version of the book..."
	@jupyter-book build ${CONTENT_PATH} --path-output ${BUILD_PATH} --builder pdfhtml

clean:
	echo "Cleaning up build artifacts..."
	@if [ -d ${BUILD_PATH} ]; then\
		jupyter-book clean ${CONTENT_PATH};\
	else\
		echo "No build artifacts to clean.";\
	fi

structure:
	echo "Generating book structure..."
	python  ${SCRIPT_PATH}make_structure.py --structure-file=$(STRUCTURE_PATH) --root=$(ROOT) --base-dir=${CONTENT_PATH}