#!/bin/bash
cd docs
rm -r build/*
clear
sphinx-apidoc -f -o source ../arbiscan
make html